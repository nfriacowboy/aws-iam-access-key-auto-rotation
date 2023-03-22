# (c) 2021 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
# https://aws.amazon.com/agreement/ or other written agreement between Customer
# and Amazon Web Services, Inc.

"""Config.

Provides configuration for the application.
"""

import os
from dataclasses import dataclass

# Logging configuration
import logging
log = logging.getLogger()
log.setLevel(logging.INFO)


@dataclass
class Config:
    """Configuration for the application."""

    # The account used to list accounts in the Organization
    orgListAccount = os.getenv('OrgListAccount')

    # The role used to list accounts in the Organization
    orgListRole = os.getenv('OrgListRole')

    # The IAM Role Session Name
    roleSessionName = os.getenv('RoleSessionName')

    # Flag- If lambda is running  in VPC
    runLambdaInVPC = str(os.getenv('RunLambdaInVPC')).lower() == 'true'
