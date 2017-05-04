import argparse
import subprocess

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def main():
    parser = argparse.ArgumentParser(description='mkcert')
    parser.add_argument('domains', nargs='+')

    args = parser.parse_args()

    for domain in args.domains:
        command = [
            "openssl", "req", "-x509", "-newkey", "rsa:4096", "-days", "365",
            "-sha256", "-nodes",
            "-keyout", "{}-key.pem".format(domain),
            "-out", "{}-cert.pem".format(domain),
            "-subj", "/C=FR/CN={}".format(domain),
        ]

        subprocess.check_call(command)
