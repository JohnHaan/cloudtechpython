

```python
import inspect
```


```python
import sys
from oslo_config import cfg
from oslo_log import log as logging

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = "demo"
```


```python
dir(logging)
```




    ['BaseLoggerAdapter',
     'CRITICAL',
     'DEBUG',
     'ERROR',
     'FATAL',
     'INFO',
     'KeywordArgumentAdapter',
     'LogConfigError',
     'NOTSET',
     'TRACE',
     'WARN',
     'WARNING',
     '_',
     '__builtins__',
     '__doc__',
     '__file__',
     '__name__',
     '__package__',
     '_create_logging_excepthook',
     '_find_facility',
     '_get_log_file_path',
     '_iter_loggers',
     '_load_log_config',
     '_loggers',
     '_mutate_hook',
     '_options',
     '_refresh_root_level',
     '_setup_logging_from_conf',
     'cfg',
     'formatters',
     'getLogger',
     'get_default_log_levels',
     'handlers',
     'importutils',
     'logging',
     'moves',
     'os',
     'platform',
     'register_options',
     'set_defaults',
     'setup',
     'six',
     'sys',
     'syslog',
     'tempest_set_log_file',
     'traceback']




```python
logging.register_options(CONF)
logging.setup(CONF, "demo")
```


```python
print(inspect.getsource(logging.register_options))
```

    def register_options(conf):
        """Register the command line and configuration options used by oslo.log."""
    
        # Sometimes logging occurs before logging is ready (e.g., oslo_config).
        # To avoid "No handlers could be found," temporarily log to sys.stderr.
        root_logger = logging.getLogger(None)
        if not root_logger.handlers:
            root_logger.addHandler(logging.StreamHandler())
    
        conf.register_cli_opts(_options.common_cli_opts)
        conf.register_cli_opts(_options.logging_cli_opts)
        conf.register_opts(_options.generic_log_opts)
        conf.register_opts(_options.log_opts)
        formatters._store_global_conf(conf)
    
        conf.register_mutate_hook(_mutate_hook)
    



```python
LOG.info("hello")
```

    2017-04-03 07:00:42.467 21793 INFO __main__ [-] hello



```python
LOG.warning("warnning")
```

    2017-04-03 07:01:15.180 21793 WARNING __main__ [-] warnning



```python
LOG.error("error!")
```

    2017-04-03 07:01:44.024 21793 ERROR __main__ [-] error!



```python
print inspect.getsource(LOG.info)
```

        def info(self, msg, *args, **kwargs):
            """
            Delegate an info call to the underlying logger, after adding
            contextual information from this adapter instance.
            """
            msg, kwargs = self.process(msg, kwargs)
            self.logger.info(msg, *args, **kwargs)
    



```python
LOG.info("%(key)s, %(age)d", {"key":"hello", "age":10})
```

    2017-04-03 07:12:51.923 21793 INFO __main__ [-] hello, 10



```python

```
