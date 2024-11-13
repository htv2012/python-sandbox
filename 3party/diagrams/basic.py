from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Basic"):
    ELB("ELB") >> EC2("EC2") >> RDS("RDS")
