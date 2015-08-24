# -*- coding: utf-8 -*-
from lxml.etree import XMLSyntaxError as XMLSyntaxError

import connection as UWSConnection
import models
from errors import UWSError


class Client(object):
    def __init__(self, url=None, user=None, password=None, connection=None):
        if connection:
            self.connection = connection
        else:
            self.connection = UWSConnection.Connection(url, user, password)

    def get_job_list(self):
        try:
            response = self.connection.get('')
        except Exception as e:
            raise UWSError(str(e))

        raw = response.read()

        try:
            job_list = models.Jobs(raw)
        except XMLSyntaxError as e:
            raise UWSError("Malformatted response. Are you sure the host you specified is a IVOA UWS service?", raw)
        except Exception as e:
            raise e

        return job_list

    def get_job(self, id):
        try:
            response = self.connection.get(id)
        except Exception as e:
            raise UWSError(str(e))

        raw = response.read()
        try:
            result = models.Job(raw)
        except XMLSyntaxError as e:
            raise UWSError("Malformatted response. Are you sure the host you specified is a IVOA UWS service?", raw)
        except Exception as e:
            raise e

        return result

    def new_job(self, args={}):
        try:
            response = self.connection.post('', args)
        except Exception as e:
            raise UWSError(str(e))

        raw = response.read()
        try:
            result = models.Job(raw)
        except XMLSyntaxError as e:
            raise UWSError("Malformatted response. Are you sure the host you specified is a IVOA UWS service?", raw)
        except Exception as e:
            raise

        return result

    def set_params_job(self, id, args={}):
        try:
            response = self.connection.post(id, args)
        except Exception as e:
            raise UWSError(str(e))

        raw = response.read()
        try:
            result = models.Job(raw)
        except XMLSyntaxError as e:
            raise UWSError("Malformatted response. Are you sure the host you specified is a IVOA UWS service?", raw)
        except Exception as e:
            raise e

        return result

    def run_job(self, id):
        try:
            response = self.connection.post(id, {"phase": "RUN"})
        except Exception as e:
            raise UWSError(str(e))

        raw = response.read()
        try:
            result = models.Job(raw)
        except XMLSyntaxError as e:
            raise UWSError("Malformatted response. Are you sure the host you specified is a IVOA UWS service?", raw)
        except Exception as e:
            raise e

        return result

    def abort_job(self, id):
        try:
            response = self.connection.post(id, {"phase": "abort"})
        except Exception as e:
            raise UWSError(str(e))

        raw = response.read()
        try:
            result = models.Job(raw)
        except XMLSyntaxError as e:
            raise UWSError("Malformatted response. Are you sure the host you specified is a IVOA UWS service?", raw)
        except Exception as e:
            raise e

        return result

    def delete_job(self, id):
        try:
            response = self.connection.delete(id)
        except Exception as e:
            raise UWSError(str(e))

        raw = response.read()
        try:
            result = True
        except XMLSyntaxError as e:
            raise UWSError("Malformatted response. Are you sure the host you specified is a IVOA UWS service?", raw)
        except Exception as e:
            raise e

        return result
