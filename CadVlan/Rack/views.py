# -*- coding:utf-8 -*-

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
from CadVlan.Util.Decorators import log, login_required, has_perm, access_external
from CadVlan.permissions import EQUIPMENT_MANAGEMENT
from networkapiclient.exception import EnvironmentVipNotFoundError, InvalidParameterError, NetworkAPIClientError, UserNotAuthorizedError, NumeroRackDuplicadoError 
from django.contrib import messages
from CadVlan.Auth.AuthSession import AuthSession
from CadVlan.Util.shortcuts import render_to_response_ajax
from CadVlan.templates import RACK_EDIT, RACK_FORM, RACK_VIEW_AJAX
from django.template.context import RequestContext
from CadVlan.Rack.forms import RackForm
from CadVlan.Util.utility import DataTablePaginator, validates_dict
from networkapiclient.Pagination import Pagination
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.core.context_processors import request
from django.template.context import Context, RequestContext
from CadVlan.messages import auth_messages, equip_messages, error_messages, rack_messages
from CadVlan.Util.converters.util import split_to_array

import json


logger = logging.getLogger(__name__)

def validar_mac(mac):

    if not mac=='':
        if not (mac.count(':') == 5):
            raise InvalidParameterError(u'Endereco MAC invalido. Formato: FF:FF:FF:FF:FF:FF')
        mac_val = mac.split(':')
        if ((len(mac_val[0])>2) or (len(mac_val[1])>2) or (len(mac_val[2])>2) or (len(mac_val[3])>2) or (len(mac_val[4])>2) or (len(mac_val[5])>2)):
            raise InvalidParameterError(u'Endereco MAC invalido. Formato: FF:FF:FF:FF:FF:FF')

def buscar_id_equip(client, nome):
                
    id_equip = None
    if not nome=='':
       # try:
            equip = client.create_equipamento().listar_por_nome(nome)
            equip = equip.get('equipamento')
            id_equip = equip['id']
            return (id_equip)
        #except NetworkAPIClientError, e:
         #   logger.error(e)
          #  messages.add_message(request, messages.ERROR, e)
            #raise InvalidParameterError(u'Equipamento nao esta cadastrado.')
    
def buscar_nome_equip(client, rack, tipo):
    id_equip = rack.get(tipo)
    if not id_equip==None:
        equip = client.create_equipamento().listar_por_id(id_equip)
        equip = equip.get('equipamento')
        nome_eq =  equip.get('nome')
        rack[tipo] = nome_eq
    else:
        rack[tipo] = ''


@log
@login_required
@has_perm([{"permission": EQUIPMENT_MANAGEMENT, "write": True}, ])
def rack_form(request):
   
    try:

        auth = AuthSession(request.session)
        client = auth.get_clientFactory()

        if request.method == 'POST':

            form = RackForm(request.POST)
            
            if form.is_valid():
                rack_number = form.cleaned_data['rack_number']
                mac_sw1 = form.cleaned_data['mac_address_sw1']
                mac_sw2 = form.cleaned_data['mac_address_sw2']
                mac_ilo = form.cleaned_data['mac_address_ilo']
                nome_sw1 = form.cleaned_data['nome_sw1']
                nome_sw2 = form.cleaned_data['nome_sw2']
                nome_ilo = form.cleaned_data['nome_ilo']

                # Validacao: MAC 
                validar_mac(mac_sw1)
                validar_mac(mac_sw2)
                validar_mac(mac_ilo)
                
                id_sw1 = buscar_id_equip(client,nome_sw1)
                id_sw2 = buscar_id_equip(client,nome_sw2)
                id_ilo = buscar_id_equip(client,nome_ilo)
 
                rack = client.create_rack().insert_rack(rack_number, mac_sw1, mac_sw2, mac_ilo, id_sw1, id_sw2, id_ilo)
                messages.add_message(request, messages.SUCCESS, rack_messages.get("success_insert"))
                return render_to_response(RACK_FORM, {'form': form}, context_instance=RequestContext(request))

        else:
            form = RackForm()

    except NetworkAPIClientError, e:
        logger.error(e)
        messages.add_message(request, messages.ERROR, e)
    return render_to_response(RACK_FORM, {'form': form}, context_instance=RequestContext(request))


@log
@login_required
@has_perm([{"permission": EQUIPMENT_MANAGEMENT, "read": True}, {"permission": EQUIPMENT_MANAGEMENT, "write": True}])
def ajax_view(request):

    # Get user
    auth = AuthSession(request.session)
    client_api = auth.get_clientFactory()

    return ajax_rack_view(request, client_api)


def ajax_rack_view(request, client_api):

    try:

        racks = dict()

        # Get all racks from NetworkAPI
        racks = client_api.create_rack().find_racks()

        if not racks.has_key("rack"):
                    racks["rack"] = []

        rack = racks.get('rack')

        for var in rack:
            mac_1 = var.get("mac_sw1")           
            mac_2 = var.get("mac_sw2")           
            mac_3 = var.get("mac_ilo")
           
            buscar_nome_equip(client_api, var, 'id_sw1')
            buscar_nome_equip(client_api, var, 'id_sw2')
            buscar_nome_equip(client_api, var, 'id_ilo')

            if mac_1==None:
                var['mac_sw1'] = ''
            if mac_2==None:
                var['mac_sw2'] = ''
            if mac_3==None:
                var['mac_ilo'] = ''

    except NetworkAPIClientError, e:
        logger.error(e)
        messages.add_message(request, messages.ERROR, e)

    return render_to_response(RACK_VIEW_AJAX, racks, context_instance=RequestContext(request))


@log
@login_required
@has_perm([{"permission": EQUIPMENT_MANAGEMENT, "write": True}, ])
def rack_edit(request, id_rack):

    lists = dict()
    lists['id'] = id_rack

    try:
        auth = AuthSession(request.session)
        client = auth.get_clientFactory()

        # Get all racks from NetworkAPI
        racks = client.create_rack().find_racks()

        if not racks.has_key("rack"):
                    racks["rack"] = []

        rackn = racks.get('rack')
        for var in rackn:
            if (var['id']==id_rack):
                rack = var

        if request.method == 'GET':

            nome_eq1 = buscar_nome_equip(client, rack, 'id_sw1')
            nome_eq2 = buscar_nome_equip(client, rack, 'id_sw2')
            nome_eq3 = buscar_nome_equip(client, rack, 'id_ilo')
            lists['numero'] = rack.get('numero')

            lists['form'] = RackForm(initial={'rack_number': rack.get('numero'), "mac_address_sw1": rack.get('mac_sw1'), "mac_address_sw2": rack.get(
                "mac_sw2"), "mac_address_ilo": rack.get('mac_ilo'), "nome_sw1": rack.get('id_sw1'), "nome_sw2": rack.get('id_sw2'), "nome_ilo": rack.get('id_ilo')})

        if request.method == 'POST':
            form = RackForm(request.POST)
            lists['form'] = form

            if form.is_valid():
                numero = form.cleaned_data['rack_number']
                mac_sw1 = form.cleaned_data['mac_address_sw1']
                mac_sw2 = form.cleaned_data['mac_address_sw2']
                mac_ilo = form.cleaned_data['mac_address_ilo']
                nome_sw1 = form.cleaned_data['nome_sw1']
                nome_sw2 = form.cleaned_data['nome_sw2']
                nome_ilo = form.cleaned_data['nome_ilo']

                # Validacao: MAC 
                validar_mac(mac_sw1)
                validar_mac(mac_sw2)
                validar_mac(mac_ilo)

                id_sw1 = buscar_id_equip(client,nome_sw1)
                id_sw2 = buscar_id_equip(client,nome_sw2)
                id_ilo = buscar_id_equip(client,nome_ilo)

                rack = client.create_rack().edit_rack(id_rack, rack.get('numero'), mac_sw1, mac_sw2, mac_ilo, id_sw1, id_sw2, id_ilo)
                messages.add_message(request, messages.SUCCESS, rack_messages.get("success_edit"))

                return render_to_response(RACK_EDIT, lists, context_instance=RequestContext(request))

    except NetworkAPIClientError, e:
        logger.error(e)
        messages.add_message(request, messages.ERROR, e)

    return render_to_response(RACK_EDIT, lists, context_instance=RequestContext(request))
