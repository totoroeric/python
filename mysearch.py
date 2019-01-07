# -*- coding:UTF-8 -*-
import ldap
conn = ldap.initialize('ldap://172.16.1.16')
rest = conn.simple_bind_s('CN=hgadread,OU=SysAccounts,OU=TFAccounts,DC=etransfar,DC=com','StBW3uFnwBGP')
def my_search(my_filter='',my_attr=None):
    conn = ldap.initialize('ldap://172.16.1.16')
    rest = conn.simple_bind_s('CN=hgadread,OU=SysAccounts,OU=TFAccounts,DC=etransfar,DC=com','StBW3uFnwBGP')
    result_id = conn.search('ou=全体人员,dc=etransfar,dc=com',ldap.SCOPE_SUBTREE,my_filter,my_attr)
    result_type,result_data = conn.result(result_id)
    return result_data

