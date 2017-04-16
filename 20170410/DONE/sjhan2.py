## neutron.plugin.ml2.drivers.type_tunnek.TunnelTypeDriver

class TunnelTypeDriver(helpers.SegmentTypeDriver):
    """Define stable abstract interface for ML2 type drivers.

    tunnel type networks rely on tunnel endpoints. This class defines abstract
    methods to manage these endpoints.
    """
    BULK_SIZE = 100

    def __init__(self, model):
        super(TunnelTypeDriver, self).__init__(model)
        self.segmentation_key = next(iter(self.primary_keys))
        
## neutron.plugin.ml2.drivers.type_tunnek.EndpointTunnelTypeDriver

class EndpointTunnelTypeDriver(TunnelTypeDriver):

    def __init__(self, segment_model, endpoint_model):
        super(EndpointTunnelTypeDriver, self).__init__(segment_model)
        self.endpoint_model = endpoint_model
        self.segmentation_key = next(iter(self.primary_keys))

## neutron.plugin.ml2.drivers.type_vxlan.VxlanTypeDriver

class VxlanTypeDriver(type_tunnel.EndpointTunnelTypeDriver):

    def __init__(self):
        super(VxlanTypeDriver, self).__init__(
            VxlanAllocation, VxlanEndpoints)