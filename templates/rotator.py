
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------
# rotator.py - Alpaca API responders for Rotator
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
class RotatorMetadata:
    """ Metadata describing the Rotator Device. Edit for your device"""
    Name = 'Sample Rotator'
    Version = '##DRIVER VERSION AS STRING##'
    Description = 'My ASCOM Rotator'
    DeviceType = 'Rotator'
    DeviceID = '##GENERATE A NEW GUID AND PASTE HERE##' # https://guidgenerator.com/online-guid-generator.aspx
    Info = 'Alpaca Sample Device\nImplements IRotator\nASCOM Initiative'
    MaxDeviceNumber = maxdev
    InterfaceVersion = ##YOUR DEVICE INTERFACE VERSION##        # IRotatorVxxx

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
            resp.text = MethodResponse(req, DriverException(0x500, 'Rotator.Connected failed', ex)).json

@before(PreProcessRequest(maxdev))
class description:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(RotatorMetadata.Description, req).json

@before(PreProcessRequest(maxdev))
class driverinfo:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(RotatorMetadata.Info, req).json

@before(PreProcessRequest(maxdev))
class interfaceversion:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(RotatorMetadata.InterfaceVersion, req).json

@before(PreProcessRequest(maxdev))
class driverversion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(RotatorMetadata.Version, req).json

@before(PreProcessRequest(maxdev))
class name():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(RotatorMetadata.Name, req).json

@before(PreProcessRequest(maxdev))
class supportedactions:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse([], req).json  # Not PropertyNotImplemented

@before(PreProcessRequest(maxdev))
class canreverse:

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
                            DriverException(0x500, 'Rotator.Canreverse failed', ex)).json

@before(PreProcessRequest(maxdev))
class ismoving:

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
                            DriverException(0x500, 'Rotator.Ismoving failed', ex)).json

@before(PreProcessRequest(maxdev))
class mechanicalposition:

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
                            DriverException(0x500, 'Rotator.Mechanicalposition failed', ex)).json

@before(PreProcessRequest(maxdev))
class position:

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
                            DriverException(0x500, 'Rotator.Position failed', ex)).json

@before(PreProcessRequest(maxdev))
class reverse:

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
                            DriverException(0x500, 'Rotator.Reverse failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        reversestr = get_request_field('Reverse', req)      # Raises 400 bad request if missing
        reverse = to_bool(reversestr)                       # Same here

        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Rotator.Reverse failed', ex)).json

@before(PreProcessRequest(maxdev))
class stepsize:

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
                            DriverException(0x500, 'Rotator.Stepsize failed', ex)).json

@before(PreProcessRequest(maxdev))
class targetposition:

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
                            DriverException(0x500, 'Rotator.Targetposition failed', ex)).json

@before(PreProcessRequest(maxdev))
class halt:

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
                            DriverException(0x500, 'Rotator.Halt failed', ex)).json

@before(PreProcessRequest(maxdev))
class move:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        positionstr = get_request_field('Position', req)      # Raises 400 bad request if missing
        try:
            position = float(positionstr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Position " + positionstr + " not a valid number.')).json
            return
        ### RANGE CHECK AS NEEDED ###         # Raise Alpaca InvalidValueException with details!
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Rotator.Move failed', ex)).json

@before(PreProcessRequest(maxdev))
class moveabsolute:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        positionstr = get_request_field('Position', req)      # Raises 400 bad request if missing
        try:
            position = float(positionstr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Position " + positionstr + " not a valid number.')).json
            return
        ### RANGE CHECK AS NEEDED ###         # Raise Alpaca InvalidValueException with details!
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Rotator.Moveabsolute failed', ex)).json

@before(PreProcessRequest(maxdev))
class movemechanical:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        positionstr = get_request_field('Position', req)      # Raises 400 bad request if missing
        try:
            position = float(positionstr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Position " + positionstr + " not a valid number.')).json
            return
        ### RANGE CHECK AS NEEDED ###         # Raise Alpaca InvalidValueException with details!
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Rotator.Movemechanical failed', ex)).json

@before(PreProcessRequest(maxdev))
class sync:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        positionstr = get_request_field('Position', req)      # Raises 400 bad request if missing
        try:
            position = float(positionstr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Position " + positionstr + " not a valid number.')).json
            return
        ### RANGE CHECK AS NEEDED ###         # Raise Alpaca InvalidValueException with details!
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Rotator.Sync failed', ex)).json

