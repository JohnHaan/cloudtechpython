# _*_ coding:utf-8 _*_

#1. Car class를 활용하여, taxi, truck, bus의 각각의 특성에 맞는 객체 인스턴스를 생성하는 프로그램을 만드시오.
#  - taxi 특성 : 주황색, 4인승, 소형
#  - truck 특성 : 초록색, 2인승, 중형
#  - bus 특성 : 파란색, 15인승, 대형
#  


class Car(object):
    def __init__(self, color, howmany, size):
        self.color = color
        self.howmany = howmany
        self.size = size
        print(self.color, self.howmany, self.size)

taxi = Car("주황색", "4", "소형")
truck = Car("초록색", "2", "중형")
bus = Car("파란색", "15", "대형")


#2. OpenStack의 neutron project에서 class를 정의하는 코드를 2개 이상 찾아 코드를 붙여넣고 생성자 등을 설명하여라.
#  - github URL : https://github.com/openstack/neutron.git

1-1
neutron/neutron/agent/l2/agent_extension.py
import abc

import six

from neutron.agent.l2 import l2_agent_extension


@six.add_metaclass(abc.ABCMeta)
class AgentCoreResourceExtension(l2_agent_extension.L2AgentExtension):
    """This is a shim around L2AgentExtension class.  It is intended for use by
    out of tree extensions that were inheriting AgentCoreResourceExtension.
    """

1-2
neutron/neutron/agent/l2/l2_agent_extension.py
@six.add_metaclass(abc.ABCMeta)
class L2AgentExtension(agent_extension.AgentExtension):
    """Define stable abstract interface for l2 agent extensions.
    An agent extension extends the agent core functionality.
    """

    def initialize(self, connection, driver_type):
        """Initialize agent extension."""

    @abc.abstractmethod
    def handle_port(self, context, data):
        """Handle agent extension for port.
        This can be called on either create or update, depending on the
        code flow. Thus, it's this function's responsibility to check what
        actually changed.
        :param context: rpc context
        :param data: port data
        """

    @abc.abstractmethod
    def delete_port(self, context, data):
        """Delete port from agent extension.
        :param context: rpc context
        :param data: port data
        """

1-3
neutron/neutron/agent/agent_extension.py
@six.add_metaclass(abc.ABCMeta)
class AgentExtension(object):
    """Define stable abstract interface for agent extensions.
    An agent extension extends the agent core functionality.
    """

    @abc.abstractmethod
    def initialize(self, connection, driver_type):
        """Perform agent core resource extension initialization.
        :param connection: RPC connection that can be reused by the extension
                           to define its RPC endpoints
        :param driver_type: a string that defines the agent type to the
                            extension. Can be used to choose the right backend
                            implementation.
        Called after all extensions have been loaded.
        No resource (port, policy, router, etc.) handling will be called before
        this method.
        """

    def consume_api(self, agent_api):
        """Consume the AgentAPI instance from the AgentExtensionsManager.
        Allows an extension to gain access to resources internal to the
        neutron agent and otherwise unavailable to the extension.  Examples of
        such resources include bridges, ports, and routers.
        :param agent_api: An instance of an agent-specific API.
        """
 