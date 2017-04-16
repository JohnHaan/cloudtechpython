#neutron/agent/ovsdb/native/commands.py
class BaseCommand(api.Command):
	    def __init__(self, api):
	        self.api = api
	        self.result = None

#neutron/worker.py
class NeutronWorker(service.ServiceBase):
    """Partial implementation of the ServiceBase ABC
    Subclasses will still need to add the other abstract methods defined in
    service.ServiceBase. See oslo_service for more details.
    If a plugin needs to handle synchronization with the Neutron database and
    do this only once instead of in every API worker, for instance, it would
    define a NeutronWorker class and the plugin would have get_workers return
    an array of NeutronWorker instances. For example:
        class MyPlugin(...):
            def get_workers(self):
                return [MyPluginWorker()]
        class MyPluginWorker(NeutronWorker):
            def start(self):
                super(MyPluginWorker, self).start()
                do_sync()
    """

    # default class value for case when super().__init__ is not called
    _worker_process_count = 1

    def __init__(self, worker_process_count=_worker_process_count):
        """
        Initialize worker
        :param worker_process_count: Defines how many processes to spawn for
            worker:
                0 - spawn 1 new worker thread,
                1..N - spawn N new worker processes
        """
        self._worker_process_count = worker_process_count