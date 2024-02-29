from snirk.sni import sni_pb2 as pb
from snirk.sni import sni_pb2_grpc as sni


def test_pb():
    """Coherence check that sni_pb2 is importable."""
    assert pb.DESCRIPTOR


def test_sni():
    """Coherence check that sni_pb2_grpc is importable."""
    assert bool(sni.Devices)
