volatildap
==========


.. image:: https://secure.travis-ci.org/rbarrois/volatildap.png?branch=master
    :target: http://travis-ci.org/rbarrois/volatildap/

.. image:: https://img.shields.io/pypi/v/volatildap.svg
    :target: https://pypi.python.org/pypi/volatildap/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/volatildap.svg
    :target: https://pypi.python.org/pypi/volatildap/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/wheel/volatildap.svg
    :target: https://pypi.python.org/pypi/volatildap/
    :alt: Wheel status

.. image:: https://img.shields.io/pypi/l/volatildap.svg
    :target: https://pypi.python.org/pypi/volatildap/
    :alt: License

``volatildap`` provides simple helpers for testing code against a LDAP database.

Its main features include:

* **Simple configuration:** Don't provide anything; the LDAP server will start with sane defaults
* **Built-in cleanup:** As soon as the test ends / the test process exits, the server is instantly removed
* **Cross-distribution setup:** Automatically discover system paths for OpenLDAP binaries, schemas, etc.


Usage
-----

.. code-block:: python

    import volatildap

    class MyTests(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            super(MyTests, cls).setUpClass()
            cls._slapd = volatildap.LdapServer(suffix='dc=example,dc=org')

        def setUp(self):
            # Will start the server, or reset/restart it if already started from a previous test.
            self._slapd.start()

        def test_something(self):
            conn = ldap.connection(self._slapd.uri)
            # Do some tests

        def test_with_data(self):
            # Load some data
            self._slapd.add({'ou=people': {'cn': [b'Users']}})
            # Run the tests


The ``volatildap.LdapServer`` provides a few useful methods:

``start()``
    Start or restart the server.
    This will:

    * Clear all data, if any
    * Start the server if it's not yet running
    * Populate the initial data

``stop()``
    Stop the server.

    This will clean up all data and kill the proces.

``wait()``
    Wait until the server is asked to stop.

    Mostly useful when controlling the server in another manner, or to use the volatildap
    server as a development instance.

``add(data)``
    Add some data, see the ``initial_data`` structure below.

``get(dn)``
    Retrieve an object by its distinguished name;

    Returns a dictionary mapping an attribute to the list of its values, as bytes.

    Raises ``KeyError`` if the distinguished name is unknown to the underlying database.

``add_ldif(contents)``
    Add lines from a LDIF file - contents should be bytes.

``get_ldif(dn)``
    Return an entry as a list of lines for a LDIF file

``reset()``
    Restore the server to its pristine, initial state.
    This includes loading the inital_data.


It also exposes the following attributes:

``uri``
    The URI to use to contect the server (e.g ``ldap://localhost:10389/``)

``rootdn``
    The distinguishedName of the admin account

``rootpw``
    The password of the admin account

``suffix``
    The suffix used by the LDAP server

``port``
    The TCP port the LDAP server is listening on

``host``
    The hostname the LDAP server is listening on

``tls_config``
    A named tuple, containing the TLS attributes.
    The only guaranteed attribute is ``tls_config.root``, which contains the PEM-formatted
    server certificate.


Configuration
-------------

The ``volatildap.LdapServer`` class accepts a few parameters:

``suffix``
    The suffix to use for the LDAP tree
    
    *Default:* ``dc=example,dc=org``

``rootdn``
    The administrator account for the LDAP server
    
    *Default:* ``cn=testadmin,dc=example,dc=org``

``rootpw``
    The administrator password.
    
    *Default:* A random value, available through ``LdapServer.rootpw``

``schemas``
    List of schemas to load; can be either a simple name (e.g ``cosine.schema``; looked up in openldap installation); or a path to a custom one.
    
    *Default:* ``['core.schema']``

``initial_data``
    Dict mapping a distinguished name to a dict of attribute/values:

    .. code-block:: python

        slapd(initial_data={
            'ou=people': {
                'objectClass': ['organizationalUnit'],
                'cn': ['People'],
            },
        })

    **Note:** When adding data, the suffix can be omitted on objects DNs.

    *Default:* ``{}``

``skip_missing_schemas``
    When loading schemas, this flag instructs ``volatildap`` to continue if some schemas
    can't be found.
    
    *Default:* ``False``

``port``
    The port to use.

    *Default:* An available TCP port on the system

``host``
    The hostname or IP to listen on.

    *Default:* ``localhost``

``slapd_debug``
    The debug level for slapd; see ``slapd.conf``

    *Default:* ``0``

``max_server_startup_delay``
    The maximum delay allowed for server startup, in seconds.

    *Default:* ``30``

``tls_config``
    A set of TLS certificate files for configuring the server.
    A valid set for ``localhost`` is provided as ``volatildap.LOCALHOST_TLS_CONFIG``, but users may also provide their own:

    .. code-block:: python

      tls_config = volatildap.TLSConfig(
         root=read(ca_path),
         chain=[
            read(intermediate_path),
         ],
         certificate=read(certificate_path),
         key=read(key_path),
      )


Command line
------------

volatildap provides a command line entrypoint for simplicity: ``python -m volatildap.cli``

Its usage follows:

.. code-block::

    usage: cli.py [-h] [--port PORT] [--host HOST] [--suffix SUFFIX]
                  [--rootdn ROOTDN] [--rootpw ROOTPW] [--debug DEBUG]
                  [--control CONTROL] [--initial INITIAL]
                  [--schemas [SCHEMAS [SCHEMAS ...]]] [--tls]

    optional arguments:
      -h, --help            show this help message and exit
      --port PORT           Port to listen on; empty for a dynamic port
      --host HOST           Host to listen on; defaults to localhost
      --suffix SUFFIX       LDAP suffix
      --rootdn ROOTDN       Distinguished Name of LDAP admin user
      --rootpw ROOTPW       Password of LDAP admin user
      --debug DEBUG         slapd debug level
      --control CONTROL     Start the HTTP control server on this address
      --initial INITIAL     Load initial objects from the provided LDIF file
      --schemas [SCHEMAS [SCHEMAS ...]]
			    Schemas to load (multi-valued)
      --tls                 Enable TLS, using a built-in stack


Remote control
--------------

Once such a server has been started, if a control server has been provided
(for instance as ``--control :10380``), it is possible to start a Python proxy to control it:

.. code-block::

    def setUpClass(cls):
	super().setUpClass()
        cls._slapd = volatildap.ProxyServer('http://localhost:10380')

All commands available on a normal instance will be available on the proxy:
``reset``, ``start``, ``stop``, ``add``, ``add_ldif``, ``get``, ``get_ldif``.

The readonly attributes are also available: ``uri``, ``suffix``, ``rootdn``,
``rootpw``, ``port``, ``host``, ``tls_config``.

When using TLS, the server's root certificate authority can be accessed
through ``proxy.tls_config.root``.


Per-distribution specificities
------------------------------

Ubuntu
    Under Ubuntu, the default AppArmor policy does not allow ``slapd`` (the LDAP daemon) to read temporary folders.
    Users should update the ``/etc/apparmor.d/local/usr.sbin.slapd`` file:

    .. code-block::

        # Allow reading, writing and locking files under /tmp
        /tmp/** rwk,
        # Allow reading development files
        /home/** rw,

    Then, reload apparmor with `systemctl reload apparmor`.
