
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------
# dome.py - Alpaca API responders for Dome
#
# Author:   Your R. Name <your@email.org> (abc)
#
# -----------------------------------------------------------------------------
# Edit History:
#   Generated by Python Interface Generator for AlpycaDevice
#
# ??-???-????   abc Initial edit

from falcon import Request, Response, HTTPBadRequest, before
from logging import Logger
from shr import PropertyResponse, MethodResponse, PreProcessRequest, \
                get_request_field, to_bool
from exceptions import *        # Nothing but exception classes

logger: Logger = None

# ----------------------
# MULTI-INSTANCE SUPPORT
# ----------------------
# If this is > 0 then it means that multiple devices of this type are supported.
# Each responder on_get() and on_put() is called with a devnum parameter to indicate
# which instance of the device (0-based) is being called by the client. Leave this
# set to 0 for the simple case of controlling only one instance of this device type.
#
maxdev = 0                      # Single instance

# -----------
# DEVICE INFO
# -----------
# Static metadata not subject to configuration changes
## EDIT FOR YOUR DEVICE ##
class DomeMetadata:
    """ Metadata describing the Dome Device. Edit for your device"""
    Name = 'Sample Dome'
    Version = '##DRIVER VERSION AS STRING##'
    Description = 'My ASCOM Dome'
    DeviceType = 'Dome'
    DeviceID = '##GENERATE A NEW GUID AND PASTE HERE##' # https://guidgenerator.com/online-guid-generator.aspx
    Info = 'Alpaca Sample Device\nImplements IDome\nASCOM Initiative'
    MaxDeviceNumber = maxdev
    InterfaceVersion = ##YOUR DEVICE INTERFACE VERSION##        # IDomeVxxx

# --------------------
# RESOURCE CONTROLLERS
# --------------------

@before(PreProcessRequest(maxdev))
class action:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class commandblind:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class commandbool:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class commandstring:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class connected:
    def on_get(self, req: Request, resp: Response, devnum: int):
            # -------------------------------
            is_conn = ### READ CONN STATE ###
            # -------------------------------
        resp.text = PropertyResponse(is_conn, req).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        conn_str = get_request_field('Connected', req)
        conn = to_bool(conn_str)              # Raises 400 Bad Request if str to bool fails
        try:
            # --------------------------------
            ### CONNECT/DISCONNECT()PARAM) ###
            # --------------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req, DriverException(0x500, 'Dome.Connected failed', ex)).json

@before(PreProcessRequest(maxdev))
class description:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(DomeMetadata.Description, req).json

@before(PreProcessRequest(maxdev))
class driverinfo:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(DomeMetadata.Info, req).json

@before(PreProcessRequest(maxdev))
class interfaceversion:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(DomeMetadata.InterfaceVersion, req).json

@before(PreProcessRequest(maxdev))
class driverversion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(DomeMetadata.Version, req).json

@before(PreProcessRequest(maxdev))
class name():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(DomeMetadata.Name, req).json

@before(PreProcessRequest(maxdev))
class supportedactions:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse([], req).json  # Not PropertyNotImplemented

@before(PreProcessRequest(maxdev))
class altitude:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Altitude failed', ex)).json

@before(PreProcessRequest(maxdev))
class athome:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Athome failed', ex)).json

@before(PreProcessRequest(maxdev))
class atpark:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Atpark failed', ex)).json

@before(PreProcessRequest(maxdev))
class azimuth:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Azimuth failed', ex)).json

@before(PreProcessRequest(maxdev))
class canfindhome:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Canfindhome failed', ex)).json

@before(PreProcessRequest(maxdev))
class canpark:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Canpark failed', ex)).json

@before(PreProcessRequest(maxdev))
class cansetaltitude:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Cansetaltitude failed', ex)).json

@before(PreProcessRequest(maxdev))
class cansetazimuth:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Cansetazimuth failed', ex)).json

@before(PreProcessRequest(maxdev))
class cansetpark:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Cansetpark failed', ex)).json

@before(PreProcessRequest(maxdev))
class cansetshutter:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Cansetshutter failed', ex)).json

@before(PreProcessRequest(maxdev))
class canslave:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Canslave failed', ex)).json

@before(PreProcessRequest(maxdev))
class cansyncazimuth:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Cansyncazimuth failed', ex)).json

@before(PreProcessRequest(maxdev))
class shutterstatus:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Shutterstatus failed', ex)).json

@before(PreProcessRequest(maxdev))
class slaved:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Slaved failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        slavedstr = get_request_field('Slaved', req)      # Raises 400 bad request if missing
        slaved = to_bool(slavedstr)                       # Same here

        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Slaved failed', ex)).json

@before(PreProcessRequest(maxdev))
class slewing:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Dome.Slewing failed', ex)).json

@before(PreProcessRequest(maxdev))
class abortslew:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Abortslew failed', ex)).json

@before(PreProcessRequest(maxdev))
class closeshutter:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Closeshutter failed', ex)).json

@before(PreProcessRequest(maxdev))
class findhome:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Findhome failed', ex)).json

@before(PreProcessRequest(maxdev))
class openshutter:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Openshutter failed', ex)).json

@before(PreProcessRequest(maxdev))
class park:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Park failed', ex)).json

@before(PreProcessRequest(maxdev))
class setpark:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Setpark failed', ex)).json

@before(PreProcessRequest(maxdev))
class slewtoaltitude:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        altitudestr = get_request_field('Altitude', req)      # Raises 400 bad request if missing
        try:
            altitude = float(altitudestr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Altitude " + altitudestr + " not a valid number.')).json
            return
        ### RANGE CHECK AS NEEDED ###         # Raise Alpaca InvalidValueException with details!
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Slewtoaltitude failed', ex)).json

@before(PreProcessRequest(maxdev))
class slewtoazimuth:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        azimuthstr = get_request_field('Azimuth', req)      # Raises 400 bad request if missing
        try:
            azimuth = int(azimuthstr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Azimuth " + azimuthstr + " not a valid number.')).json
            return
        ### RANGE CHECK AS NEEDED ###       # Raise Alpaca InvalidValueException with details!
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Slewtoazimuth failed', ex)).json

@before(PreProcessRequest(maxdev))
class synctoazimuth:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        azimuthstr = get_request_field('Azimuth', req)      # Raises 400 bad request if missing
        try:
            azimuth = int(azimuthstr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Azimuth " + azimuthstr + " not a valid number.')).json
            return
        ### RANGE CHECK AS NEEDED ###       # Raise Alpaca InvalidValueException with details!
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Dome.Synctoazimuth failed', ex)).json

