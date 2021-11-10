# -*- coding: utf-8 -*-
# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand


class UsersCommand(RESTCommand):

    resource = 'users'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def add_policy(self, user_uuid, policy_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = '{}/{}/policies/{}'.format(self.base_url, user_uuid, policy_uuid)
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def change_password(self, user_uuid, **kwargs):
        headers = self._get_headers()
        url = '/'.join([self.base_url, user_uuid, 'password'])
        r = self.session.put(url, headers=headers, json=kwargs)
        if r.status_code != 204:
            self.raise_from_response(r)

    def delete(self, user_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = '{}/{}'.format(self.base_url, user_uuid)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def edit(self, user_uuid, **kwargs):
        headers = self._get_headers(**kwargs)
        url = '{}/{}'.format(self.base_url, user_uuid)
        r = self.session.put(url, headers=headers, json=kwargs)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def get(self, user_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = '{}/{}'.format(self.base_url, user_uuid)
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def get_groups(self, user_uuid, **kwargs):
        return self._get_relation('groups', user_uuid, **kwargs)

    def get_policies(self, user_uuid, **kwargs):
        return self._get_relation('policies', user_uuid, **kwargs)

    def get_tenants(self, user_uuid, **kwargs):
        return self._get_relation('tenants', user_uuid, **kwargs)

    def get_sessions(self, user_uuid, **kwargs):
        return self._get_relation('sessions', user_uuid, **kwargs)

    def list(self, **kwargs):
        headers = self._get_headers(**kwargs)
        r = self.session.get(self.base_url, headers=headers, params=kwargs)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def new(self, **kwargs):
        headers = self._get_headers(**kwargs)
        r = self.session.post(self.base_url, headers=headers, json=kwargs)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def register(self, **kwargs):
        headers = self._get_headers()
        url = '{}/register'.format(self.base_url)
        r = self.session.post(url, headers=headers, json=kwargs)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def remove_policy(self, user_uuid, policy_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = '{}/{}/policies/{}'.format(self.base_url, user_uuid, policy_uuid)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def remove_session(self, user_uuid, session_uuid):
        headers = self._get_headers()
        url = '{}/{}/sessions/{}'.format(self.base_url, user_uuid, session_uuid)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def request_confirmation_email(self, user_uuid, email_uuid):
        headers = self._get_headers()
        url = '{}/{}/emails/{}/confirm'.format(self.base_url, user_uuid, email_uuid)
        r = self.session.get(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def reset_password(self, **kwargs):
        headers = self._get_headers()
        url = '{}/password/reset'.format(self.base_url)
        r = self.session.get(url, headers=headers, params=kwargs)
        if r.status_code != 204:
            self.raise_from_response(r)

    def set_password(self, user_uuid, password, token=None):
        url = '{}/password/reset'.format(self.base_url)
        query_string = {'user_uuid': user_uuid}
        body = {'password': password}
        headers = self._get_headers()
        if token:
            headers['X-Auth-Token'] = token

        r = self.session.post(url, headers=headers, params=query_string, json=body)
        if r.status_code != 204:
            self.raise_from_response(r)

    def update_emails(self, user_uuid, emails):
        headers = self._get_headers()
        url = '{}/{}/emails'.format(self.base_url, user_uuid)
        body = {'emails': emails}
        r = self.session.put(url, headers=headers, json=body)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def _get_relation(self, resource, user_uuid, tenant_uuid=None, **kwargs):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = '{}/{}/{}'.format(self.base_url, user_uuid, resource)
        r = self.session.get(url, headers=headers, params=kwargs)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()
