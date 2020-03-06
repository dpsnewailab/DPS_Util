import cv2

THUMBNAIL_RESOLUTION = (160, 160)
SD_RESOLUTION = (640, 360)
SVGA_RESOLUTION = (800, 600)
XGA_RESOLUTION = (1024, 768)
WXGA_RESOLUTION = (1280, 720)
HD_RESOLUTION = (1366, 768)
HDP_RESOLUTION = (1600, 900)
FHD_RESOLUTION = (1920, 1080)
QHD_RESOLUTION = (2560, 1440)
UHD_RESOLUTION = (3840, 2160)

PX_RGB = 0
PX_BGR = 1

HIGH_QUALITY = 100
DEFAULT_QUALITY = 95
BALANCE_QUALITY = 85
MEDIUM_QUALITY = 70
LOW_QUALITY = 60
THUMBNAIL_QUALITY = 30

IMTYPE_DEFAULT = cv2.IMREAD_ANYCOLOR
INTER_DEFAULT = cv2.INTER_CUBIC

ENCODE_JPEG = ".jpg"
ENCODE_PNG = ".png"

__all__ = ['THUMBNAIL_RESOLUTION', 'SD_RESOLUTION', 'SVGA_RESOLUTION', 'XGA_RESOLUTION', 'WXGA_RESOLUTION',
           'HD_RESOLUTION', 'HDP_RESOLUTION', 'FHD_RESOLUTION', 'QHD_RESOLUTION', 'UHD_RESOLUTION', 'PX_RGB', 'PX_BGR',
           'HIGH_QUALITY', 'DEFAULT_QUALITY', 'BALANCE_QUALITY', 'MEDIUM_QUALITY', 'LOW_QUALITY', 'THUMBNAIL_QUALITY',
           'IMTYPE_DEFAULT', 'INTER_DEFAULT', 'ENCODE_JPEG', 'ENCODE_PNG']
