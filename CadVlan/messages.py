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

error_messages = {
    'required': u'Este campo é obrigatório.',
    'max_length': u'Este campo tem que ter no máximo %(limit_value)s caracteres.',
    'min_length': u'Este campo tem que ter no mínimo %(limit_value)s caracteres.',
    'invalid_choice': u'Opção inválida selecionada.',
    'can_not_remove_all': u'Não foi possível excluir nenhum dos itens selecionados.',
    'can_not_remove': u'Não foi possível excluir alguns dos itens selecionados: %s.',
    'can_not_remove_error': u'A exclusão dos itens selecionados não foi concluída.',
    'select_one': u'Nenhum item foi selecionado.',
    'invalid_param': u'Valor do %s nulo ou inválido.',
    'vlan_select_one': u'Vlan já criada, selecione ao menos uma Rede',
    'login_required': u'Você precisa estar logado para continuar. Clique <a href="/">aqui</a> para fazer login.'
}

auth_messages = {
    'user_not_authorized': u'Usuário não autorizado para acessar/executar esta operação.',
    'user_invalid': u'Usuário e/ou senha incorretos.',
    '404': u'Página não encontrada: [URL: %s]',
    '500': u'Ocorreu um erro ao executar sua ação, contate o Administrador do sistema.',
    'user_email_invalid': u'Usuário e/ou email incorretos.',
    'email_success': u'Nova senha enviada com sucesso.',
    'pass_change_sucess': u'Senha alterada com sucesso.',
    'email_error': u'Ocorreu um erro ao enviar email.',
    'nogroup_error': u'Somente usuários que pertecem à algum grupo, podem efetuar login no sistema. ',
    'token_invalid': u'O seu tempo de acesso expirou. Por favor, atualize a página.',
    'user_ldap_not_found': u'Usuário de rede não encontrado.',
    'user_ldap_cant_recover_pass': u'Função não disponível para usuários de rede. Contate o administrador.',
    'token_required': u'Informe o token de acesso.',
}

script_messages = {
    'success_remove': u'Todos os roteiros selecionados foram excluídos com sucesso.',
    'success_insert': u'Roteiro incluído com sucesso.',
    'error_equal_name': u'Roteiro com o nome %s já cadastrado.',
    'success_edit': u'Roteiro alterado com sucesso.'
}

script_type_messages = {
    'success_remove': u'Todos os tipos de roteiros selecionados foram excluídos com sucesso.',
    'success_insert': u'Tipo de Roteiro incluído com sucesso.',
}

rack_messages = {
    'success_remove': u'Todos os Racks selecionados foram excluídos com sucesso.',
    'success_insert': u'Rack incluído com sucesso.',
    'error_equal_number': u'Numero já cadastrado.',
    'success_edit': u'Rack alterado com sucesso.',
    'sucess_create_config': u'Os arquivos de configuracao do rack %s foram criados com sucesso.',
    'can_not_create_all': u'Os arquivos de configuracao do rack %s nao foram gerados.',
    'can_not_create_config': u'Os arquivos de configuracao do %s nao pode(m) ser gerado(s)',
    'sucess_aplicar_config': u'A configuracao foi aplicada nos equipamentos do rack %s.',
    'can_not_aplicar_config': u'A configuracao não pode ser aplicada nos equipamentos do rack.',
    'sucess_alocar_config': u'Os ambientes, vlans e redes do rack %s foram alocadas com sucesso.',
    'can_not_alocar_config': u'Os ambientes, vlans e redes do rack %s não puderam ser alocadas.',
    'sucess-foreman': u'O ambiente foi registrado no Foreman.'
}

equip_access_messages = {
    'success_remove': u'Todos os acessos selecionados foram excluídos com sucesso.',
    'success_insert': u'Acesso incluído com sucesso.',
    'already_association': u'Equipamento e Protocolo já associados',
    'invalid_equip_acess': u'Equipamento Acesso inválido',
    'success_edit': u'Acesso alterado com sucesso.',
    'no_equip': u'Selecione um equipamento.',
}

equip_script_messages = {
    'success_remove': u'Todos os roteiros selecionados foram excluídos com sucesso.',
    'success_insert': u'Roteiro associado com sucesso.',
    'error_equal_ass': u'O roteiro selecionado já está associado à este equipamento.',
}

equip_interface_messages = {
    'success_insert': u'Interface incluída com sucesso.',
    'success_edit': u'Interface alterada com sucesso.',
    'success_connect': u'Interface conectada com sucesso.',
    'success_disconnect': u'Interface disconectada com sucesso.',
    'success_remove': u'Todas as interfaces selecionadas foram excluídas com sucesso.',
    'success_remove_channel': u'Channel excluido com sucesso.',
    'brand_error': u'Incluir várias interfaces não disponível para este equipamento.',
    'name_error': u'Início deve ser menor que Final.',
    'validation_error': u'Erro na validação dos dados de Interface, verifique se o campo inicial é menor que o campo final, ou se os campos foram preenchidos da maneira correta.',
    'several_sucess': u'Todas interfaces foram cadastradas com sucesso.',
    'several_warning': u'Estas interfaces já se encontravam cadastradas: %s. Todas as outras foram registradas com sucesso.',
    'several_error': u'Interfaces já cadastradas: %s.',
    'success_insert_channel': u'Port Channel incluído com sucesso.',
    'success_associando_amb': u'Ambientes associados à interface.',
    'success_edit_channel': u'Channel alterado com sucesso.',
    'success_sync': u'Configuração aplicada com sucesso.',
    'can_not_sync_error': u'Configuração não pode ser aplicada com sucesso.',
}

network_ip_messages = {
    'success_insert': u'Rede incluída com sucesso.',
    'ip_error': u'Ip não informado ou informado de forma incorreta.',
    'ip6_error': u'Ip não informado ou informado de forma incorreta. IPv6 deve ser informado no formato xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx',
    'ip_sucess': u'Ip salvo com sucesso.',
    'not_ip_in_net': u'O IP %s não pertence a network %s.',
    'ip_delete_sucess': u'Os Ips selecionados foram excluídos com sucessos.',
    'ip_edit_sucess': u'Ip alterado com sucesso.',
    'sucess_edit': u'Rede alterada com sucesso.',
    'ip_equip_delete': u'Ip excluído com sucesso.',
    'net_invalid': u'Rede de IP inválida.',
    'already_assoc_equip': u'Este equipamento já está associado ao ip.',
    'ip_assoc_success': u'Ip associado ao equipamento com sucesso.',
    'net_create_success': u'Rede(s) criada(s) com sucesso.',
    'networks_activated': u'Alguma(s) rede(s) selecionada(s) já está(ão) criada(s).'

}

network_messages = {
    'invalid_environment_vip': u'O ambiente Vip selecionado não está no mesmo Ambiente ou não é válido.',
}

vrf_messages = {
    'success_insert': u'Vrf incluída com sucesso.',
    'success_edit': u'Vrf alterada com sucesso.',
}

environment_messages = {
    'success_insert': u'Ambiente incluído com sucesso.',
    'success_edit': u'Ambiente alterado com sucesso.',
    'divisao_dc_sucess': u'Divisão DC inserida com sucesso.',
    'grupo_l3_sucess': u'Grupo Layer3 inserido com sucesso.',
    'ambiente_log_sucess': u'Ambiente Lógico inserido com sucesso.',
    'env_not_found': u'O(s) ambiente(s): %s não está(ão) cadastrado(s).',
    'env_associated': u'O(s) ambiente(s): %s tem algum equipamento ou vlan que não pode ser removido.',
    'invalid_id': u'Valor do id nulo ou inválido.',
    'success_delete_all': u'Remoção de ambiente realizada com sucesso.',
    'invalid_network': u'A rede informada está inválida.',
    'invalid_prefix_ipv4': u'O prefixo informado deve estar entre 0 e 32.',
    'invalid_prefix_ipv6': u'O prefixo informado deve estar entre 0 e 128.',
    'invalid_prefix': u'O prefixo informado deve ser maior que o bloco da rede.',
    'success_configuration_insert': u'Prefixo de ambiente incluído com sucesso.',
    'success_configuration_remove': u'Prefixo de ambiente excluído com sucesso.',
    'invalid_parameters': u'Parametros inválidos.',
}

equip_messages = {
    'equip_sucess': u'Equipamento inserido com sucesso',
    'equip_edit_sucess': u'Equipamento editado com sucesso',
    'success_remove': u'Todos os equipamentos selecionados foram excluídos com sucesso.',
    'orquestracao_error': u"Equipamentos que não sejam do tipo 'Servidor Virtual' não podem fazer parte do grupo 'Equipamentos Orquestração'.",
    'marca_sucess': u'Nova marca inserida com sucesso.',
    'modelo_sucess': u'Novo modelo inserido com sucesso.',
    'modelo_sucess': u'Novo modelo inserido com sucesso.',
    'error_associate_group': u'Grupo %s não pode ser associado ao equipamento pois seu grupo de usuário não tem permissão.',
    'error_disassociate_group': u'Grupo %s não pode ser desassociado ao equipamento pois seu grupo de usuário não tem permissão.',
}

vlan_messages = {
    'vlan_sucess': u'Vlan cadastrada com sucesso.',
    'success_remove': u'Todas as vlans selecionadas foram excluídas com sucesso.',
    'success_remove_network': u'Todas as redes selecionadas foram excluídas com sucesso.',
    'vlan_edit_sucess': u'Vlan alterada com sucesso.',
    'name_vlan_error': u'Nome da Vlan contém caracteres inválidos.',
    'vlan_git_error': u'Vlan excluída com sucesso mas ocorreu um erro de GIT, contate o administrador.',
    'vlan_create_success': u'Vlan criada com sucesso.',
}

option_vip_messages = {
    'success_remove': u'Todas as opções vip selecionadas foram excluídas com sucesso.',
    'success_insert': u'Opção vip incluída com sucesso.',
    'invalid_option_vip': u'Opção VIP inválida',
    'sucess_options': u'Opções Vip atualizadas com sucesso.',
    'vip_not_in_net': u'Ambiente Vip %s não pertence a rede %s.',
}

environment_vip_messages = {
    'success_remove': u'Todos os Ambientes vip selecionados foram excluídos com sucesso.',
    'success_insert': u'Ambiente vip incluído com sucesso.',
    'invalid_environment_vip': u'Ambiente VIP inválido',
    'sucess_edit': u'Ambiente vip alterado com sucesso.',
}

group_equip_messages = {
    'success_remove': u'Todos os grupos de equipamento foram excluídos com sucesso.',
    'success_insert': u'Grupo de equipamento cadastrado com sucesso.',
    'invalid_group_equipament': u'Grupo de equipamento inválido',
    'success_edit': u'Grupo de equipamento alterado com sucesso.',
}

equip_group_messages = {
    'duplicated_error': u'Grupo de Usuário selecionado já se encontra cadastrado nesse grupo de equipamento.',
    'success_remove': u'Todos os equipamentos foram desassociados do grupo de equipamento com sucesso.',
    'success_insert': u'Equipamento foi associado ao Grupo de equipamento com sucesso.',
    'invalid_equipament_group': u'Equipamento inválido',
    'sucess_group_user_equip': 'Direitos de grupos de Usuário em grupo de Equipamentos inserido com sucesso.',
    'sucess_group_user_equip_edit': 'Direitos de grupos de Usuário em grupo de Equipamentos foi editado com sucesso.',
    'can_not_remove': u'Não foi possível excluir alguns equipamentos selecionados por estarem associados apenas a este grupo. Equipamentos: %s.',
    'sucesso_user_equip_remove': u'Todos os grupos de usuários foram desassociados do grupos de equipamento com sucesso.',
}

group_user_messages = {
    'success_remove': u'Todos os Grupos de Usuário selecionados foram excluídos com sucesso.',
    'success_insert': u'Grupos de Usuário cadastrado com sucesso.',
    'invalid_group_user': u'Grupos de Usuário inválido',
    'success_edit': u'Grupos de Usuário alterado com sucesso.',
}

user_messages = {
    'success_remove': u'Todos os Usuários selecionados foram inativados com sucesso.',
    'success_insert': u'Usuário cadastrado com sucesso.',
    'success_edit': u'Usuário alterado com sucesso.',
    'ldap_offline': u'O LDAP não está disponível, não será possível associar o usuário CadVlan a um usuário do LDAP.',
}

user_group_messages = {
    'success_remove': u'Todos os Usuários selecionados foram desassociados do grupo de usuário com sucesso.',
    'success_insert': u'Usuário(s) foram associado(s) ao Grupo de usuário com sucesso.',
    'invalid_group_user': u'Usuário inválido',
}

perm_group_messages = {
    'success_remove': u'Todas as Permissões Administrativa foram excluídas com sucesso.',
    'success_insert': u'Permissão Administrativa cadastrada com sucesso.',
    'success_edit': u'Permissão Administrativa alterada com sucesso.',
    'invalid_group_user': u'Permissão Administrativa inválida',
}

object_group_perm_messages = {
    'success_edit': u'Permissão Individual alterada com sucesso.',
    'success_create': u'Permissão Individual criada com sucesso.',
    'success_delete': u'Permissão Individual removida com sucesso.'
}

object_group_perm_gen_messages = {
    'success_edit': u'Permissão Geral alterada com sucesso.',
    'success_create': u'Permissão Geral criada com sucesso.'

}

acl_messages = {
    'success_create': u'Acl criada com sucesso.',
    'success_remove': u'Acl foi excluida com sucesso.',
    'success_edit': u'Acl alterada com sucesso.',
    'success_apply': u'Acl aplicada a todos os Equipamentos com sucesso.',
    'success_validate': u'ACL IP%s validado com sucesso.',
    'error_apply': u'Não foi possível aplicar ACL a nenhum dos equipamentos selecionados.',
    'error_acl_not_exist': u'Acl não foi criada',

    'success_template_edit': u'Template alterado com sucesso.',
    'success_template_edit': u'Template criado com sucesso.',
    'field_required': u'Nome do template e Template são obrigatórios.',
    'field_duplicated': u'O arquivo %s já existe.',
    'invalid_template': u'Template inválido',
    'success_remove': u'Todas os Templates selecionados foram excluídos com sucesso.',

    'error_apply_ivalid_acl': u'Não foi possível aplicar ACL a nenhum dos equipamentos da(s) rede(s) %s, pois a ACL é inválida.',
    'seccess_apply_valid_acl': u'Acl aplicada a todos os equipamentos da(s) rede(s) %s com sucesso.',
    'error_apply_acl_for_network': u'Não foi possível aplicar ACL a nenhum dos equipamentos da(s) rede(s) %s.',
}

request_vip_messages = {
    'success_remove': u'Todas as Requisições VIP foram excluídas com sucesso.',
    'success_remove2': u'Todas as Requisições VIP foram removidas com sucesso.',
    'success_validate': u'Todas as Requisições VIP foram validadas com sucesso.',
    'success_validate_one': u'Requisição VIP validada com sucesso.',
    'success_create': u'Todas as Requisições VIP foram criadas com sucesso.',
    'success_create_one': u'Requisição VIP foi criada com sucesso.',
    'success_remove_one': u'Requisição VIP foi removida com sucesso.',
    'success_insert': u'Requisição VIP cadastrada com sucesso.',
    'success_edit': u'Requisição VIP alterada com sucesso.',
    'can_not_validate': u'Não foi possível validar alguns dos itens selecionados: %s.',
    'can_not_validate_one': u'Não foi possível validar o item.',
    'can_not_create': u'Não foi possível criar alguns dos itens selecionados: %s.',
    'can_not_create_one': u'Não foi possível criar o item.',
    'can_not_remove_one': u'Não foi possível remover o item.',
    'can_not_remove_error': u'A exclusão dos itens selecionados não foi concluída.',
    'can_not_remove': u'Não foi possível excluir alguns dos itens selecionados: %s.',
    'can_not_remove2': u'Não foi possível remover alguns dos itens selecionados: %s.',
    'can_not_edit': u'Não é possível editar Requisições VIP por estar criada.',
    'validate_before': u'Não foi possível criar alguns dos itens selecionados: %s, pois ainda não foram validados.',
    'validate_before_one': u'Não foi possível criar o item selecionado pois ainda não foi validado.',
    'can_not_remove_all': u'Não foi possível excluir nenhum dos itens selecionados.',
    'can_not_remove2_all': u'Não foi possível remover nenhum dos itens selecionados.',
    'can_not_validate_all': u'Não foi possível validar nenhum dos itens selecionados.',
    'can_not_create_all': u'Não foi possível criar nenhum dos itens selecionados.',
    'invalid_vip': u'Requisição VIP inválida.',
    'all_ready_create': u'Itens selecionados já foram criados: %s.',
    'all_ready_create_one': u'Item já foi criado.',
    'error_ports': u'Deve-se preencher todos os campos de portas.',
    'error_reals': u'Deve-se preencher todos os campos de reals.',
    'error_ports_required': u'Deve conter pelo menos 1 porta cadastrada.',
    'error_existing_reals': u'Não foi possível recuperar real server por inconsistência do banco de dados. ( %s - %s )',
    'error_existing_environment_vip': u'Não foi possível recuperar Ambiente VIP por inconsistência do banco de dados. ( %s - %s - %s )',
    'error_existing_timeout': u'Não foi possível recuperar Timeout por inconsistência do banco de dados. ( %s )',
    'error_existing_cache': u'Não foi possível recuperar Grupos de caches por inconsistência do banco de dados. ( %s )',
    'error_existing_persistence': u'Não foi possível recuperar Persistência por inconsistência do banco de dados. ( %s )',
    'error_existing_balancing': u'Não foi possível recuperar Método de balanceamento por inconsistência do banco de dados. ( %s )',
    'success_real': u'Todos os Real Server foram %ss com sucesso.',
    'can_not_real': u'Não foi possível %s alguns dos itens selecionados: %s.',
    'can_not_real_all': u'Não foi possível %s nenhum dos itens selecionados.',
    'not_created': u'Não foi possível remover alguns dos itens selecionados: %s, pois ainda não foram criados.',
    'tab_edit_error': u'Ocorreu um erro ao persistir a requisição vip que contém este %s no banco de dados.',
    'tab_edit_success': u'Alteração de %s realizada com sucesso.',
    'success_l7_save': u'Filtro L7 gravado com sucesso.',
    'success_l7_validate': u'Filtro L7 validado com sucesso.',
    'success_l7_alter': u'Filtro L7 aplicado com sucesso.',
    'success_l7_rollback': u'Rollback aplicado com sucesso.',
    'duplicate_vip': u'O valor da Porta VIP deve ser único.',
    'invalid_port': u'O número da porta deve estar entre 1 e 65535.',
    'invalid_weight': u'O valor do Peso do Real deve estar entre 0 e 4294967295.',
    'invalid_priority': u'O valor da Prioridade deve estar entre 0 e 4294967295.',
    'duplicated_value': u'Valores duplicados para Porta Real, Porta Vip e IP do Real na mesma Requisição VIP.',
    'real_remove': u'Real(s) removido(s) com sucesso.',
    'required_healthcheck': u'Healthcheck é obrigatório.'
}

access_type_messages = {
    'success_create': u'Tipo de Acesso cadastrado com sucesso.',
}

type_network_messages = {
    'success_create': u'Tipo de Rede cadastrado com sucesso.',
}

equipment_type_messages = {
    'success_create': u'Tipo de Equipamento cadastrado com sucesso.',
}

healthcheck_messages = {
    'success_create': u'Healtcheck Expect cadastrado com sucesso.',
    'error_create': u'Ocorreu um erro ao cadastrar um novo Healthcheck Expect.',
}


ldap_messages = {
    'success_remove_group': u'Todos os grupos selecionados foram excluídos com sucesso.',
    'success_insert_group': u'Grupo incluído com sucesso.',
    'success_edit_group': u'Grupo atualizado com sucesso.',
    'invalid_group': u'Grupo %s inválido ou não cadastrado.',
    'error_range_out_group': u'Este campo deve estar entre a faixa %s a %s.',
    'error_duplicated_name_group': u'Já existe um grupo cadastrado com nome %s .',
    'error_duplicated_gidNumber_group': u'Já existe um grupo cadastrado com gidNumber %s .',
    'error_duplicated_employeeNumber_group': u'Já existe um grupo cadastrado com cargo %s .',
    'error_duplicated_mail_group': u'Já existe um grupo cadastrado com E-mail %s .',

    'success_remove_sudoer': u'Todos os sudoers selecionados foram excluídos com sucesso.',
    'success_insert_sudoer': u'Sudoer incluído com sucesso.',
    'success_edit_sudoer': u'Sudoer atualizado com sucesso.',
    'invalid_sudoer': u'Sudoer %s inválido ou não cadastrado.',
    'error_duplicated_name_sudoer': u'Já existe um Sudoer cadastrado com nome %s .',

    'success_remove_user': u'Todos os usuários selecionados foram excluídos com sucesso.',
    'success_insert_user': u'Usuário incluído com sucesso.',
    'success_edit_user': u'Usuário atualizado com sucesso.',
    'success_lock_user': u'Usuário %s bloqueado com sucesso.',
    'success_unlock_user': u'Usuário %s desbloqueado com sucesso.',
    'invalid_user': u'Usuário %s inválido ou não cadastrado.',
    'error_range_out_user': u'Este campo deve estar entre a faixa %s a %s.',
    'error_duplicated_name_user': u'Já existe um usuário cadastrado com nome %s .',
    'error_duplicated_uidNumber_user': u'Já existe um usuário cadastrado com uidNumber %s .',


}

filter_messages = {
    'success_remove': u'Todos os filtros selecionados foram excluídos com sucesso.',
    'success_insert': u'Filtro incluído com sucesso.',
    'success_edit': u'Filtro atualizado com sucesso.',
}

block_messages = {
    'required': 'Existem campos obrigatórios não preenchidos.',
    'success_insert': 'Blocos incluídos com sucesso.',
    'success_edit': 'Blocos atualizados com sucesso.',
}

rule_messages = {
    'success_insert': u'Regra incluída com sucesso.',
    'success_edit': u'Regra atualizada com sucesso.',
    'success_remove': u'Todas as regras selecionadas foram excluídas com sucesso.',
    'required': 'Existem campos obrigatórios não preenchidos.',
}

pool_messages = {
    'success_remove': u'Todos os pools selecionados foram removidos com sucesso.',
    'success_delete': u'Todos os pools selecionados foram excluídos com sucesso.',
    'success_create': u'Todos os pools selecionados foram criados com sucesso.',
    'success_enable': u'Todos os pools members selecionados foram habilitados com sucesso.',
    'success_disable': u'Todos os pools members selecionados foram desabilitados com sucesso.',
    'success_status_change': u'Todos os pools members selecionados tiveram seus status alterados com sucesso.',
    'success_insert': u'Pool incluído com sucesso.',
    'success_update': u'Pool alterado com sucesso',
    'error_equal_name': u'Pool com o nome %s já cadastrado.',
    'error_port_missing': u'Quantidade de portas e equipamento difere',
    'error_same_port': u'Ips com portas iguais',
    'error_update': u'Erro ao alterar pool',
    'select_one': u'Deve adicionar ao menos um pool '
}

system_variable_messages = {
    'success_insert': u'Variável incluída com sucesso!',
    'success_update': u'Variável alterada com sucesso',
    'success_delete': u'Variável removida com sucesso'
}
