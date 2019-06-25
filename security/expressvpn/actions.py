#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf expressvpn_%s-1_amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.gz")
def install():
    shelltools.system("mkdir -p etc/systemd/system")
    shelltools.system("cp usr/lib/expressvpn/expressvpn.service etc/systemd/system/")
    shelltools.system("touch etc/default/expressvpn")
    shelltools.system("mkdir -p var/lib/expressvpn/certs")
    shelltools.system("chown root:root var/lib/expressvpn/certs")
    shelltools.system("chmod 755 var/lib/expressvpn/certs")
    shelltools.system("env LD_LIBRARY_PATH='usr/lib/expressvpn' usr/sbin/expressvpnd --workdir 'var/lib/expressvpn' generate-client-ca")
    shelltools.system("env LD_LIBRARY_PATH='usr/lib/expressvpn' usr/sbin/expressvpnd --workdir 'var/lib/expressvpn' generate-client-certs")
    shelltools.system("rm -f var/lib/expressvpn/certs/client.req")
    shelltools.system("rm -f var/lib/expressvpn/certs/clientca.srl")
    shelltools.system("chmod 644 var/lib/expressvpn/certs/client.key")

    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "var")
