# -*- coding: utf-8 -*-
# This software is distributed under the two-clause BSD license.

from .server import LdapServer, TLSConfig
from .version import VERSION as __version__

LOCALHOST_TLS_CONFIG = TLSConfig(
    root="""-----BEGIN CERTIFICATE-----
MIIDujCCAqKgAwIBAgIJAP8c4ptKOyWOMA0GCSqGSIb3DQEBCwUAMDIxIjAgBgNV
BAMMGVNlbGYtc2lnbmVkIGxvY2FsIENBIFJvb3QxDDAKBgNVBAsMA0RldjAeFw0x
OTA1MTUwOTE2MDdaFw0yOTA1MTIwOTE2MDdaMDIxIjAgBgNVBAMMGVNlbGYtc2ln
bmVkIGxvY2FsIENBIFJvb3QxDDAKBgNVBAsMA0RldjCCASIwDQYJKoZIhvcNAQEB
BQADggEPADCCAQoCggEBAKcIx6fyd9LrZhEXT+jEq4XHcW9G8NIilEAfPS+sofr5
b1kVtzgF17Qihy3gwKuaAhwHHO4pYk+gXhAyZBzR/oCnUefUVM3yAC3UeVY4LOei
vsulhwhpTyegtUVXUvV93f6tT1aEMqyc6gbZI+FQkyYR60m5qu+vIuIDPXT2yS9W
VaXvZy55aNnHK4hIqIDktOD8AL0++7VywxsMJ3IxBQ8smCPr048xoooONRNQgAuo
ZSbrFgs9njMrr2TXMi7ivBjpPH6gn1jdI7gQTVwobLmtd7gjSPISfnxhYnV0neax
oIouuQ3DTUkqmoHdVY1KodtZrRKIHZIJn02GqSlmQNECAwEAAaOB0jCBzzASBgNV
HRMBAf8ECDAGAQH/AgEBMA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUL9x+1PPT
TZoDInzjIhdvJWzeHYMwYgYDVR0jBFswWYAUL9x+1PPTTZoDInzjIhdvJWzeHYOh
NqQ0MDIxIjAgBgNVBAMMGVNlbGYtc2lnbmVkIGxvY2FsIENBIFJvb3QxDDAKBgNV
BAsMA0RldoIJAP8c4ptKOyWOMCYGA1UdHgQfMB2gGzAMggoubG9jYWxob3N0MAuC
CWxvY2FsaG9zdDANBgkqhkiG9w0BAQsFAAOCAQEAJGqg2DcnnMYnxHM8y7OTZE9p
RPs+x1K+QkOxYr8Ex8RRfpmEJy+SeIlqxqN+4TyvfH7s1Q9PKfchflpY0EsVG3jU
N2gH+OiMaGD7mzHaTWodu4qOOQ17X97exhfvJ5phcqa7Ujn2WgeVHRKMyd2HROAX
wJreY7DbznZUCYnxDb6w4PSxhwJzL/pSb9BpBmYr4bQ39bQpEqpcEqquA3jzx53Z
fUcUb7dUGZUw/fuSN5hBQBHQf31A9h4KfuysEXsNSs/UZD0Ls6VSsja6WnBdqaMX
J7S/I0YTaDvqv3Il9gqSz/XNurO0QNREHKX7F8KQPw27UYjdwHqse36fJm1LPQ==
-----END CERTIFICATE-----
""",
    chain=[
        """-----BEGIN CERTIFICATE-----
MIIDsjCCApqgAwIBAgIBAjANBgkqhkiG9w0BAQsFADAyMSIwIAYDVQQDDBlTZWxm
LXNpZ25lZCBsb2NhbCBDQSBSb290MQwwCgYDVQQLDANEZXYwHhcNMTkwNTE1MDkx
NjA3WhcNMjkwNTEyMDkxNjA3WjAyMSIwIAYDVQQDDBlTZWxmLXNpZ25lZCBsb2Nh
bCBDQSBSb290MQwwCgYDVQQLDANEZXYwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQC6JO1LTnE91L5cjmedtHmasLiBICJrzJf/PijSixEcCAIruCWu4Q5h
N2IMOJtd4hisCzLNrSk6NcNA6fM3aaiDx04Mam1Ex6pMYNHPueF4aiqxmh8m3FMU
4TgFXutMlaYWTZWjBpD66gx60/G3inYCtIoTN2wUu52w1c7d4Gj2ihGkzaVw6goM
1fXPh1wWVj/z1n2jrb5xK2Mbi0+FfKEI3ayhPhSDp7pQ8hl69HKzWMS1tBbq0TVV
PsTyj/9ITBUyV364qh65zLCM2zhdQEheeDl2hq0TSOcOZBAF+SvL6qoDboUKkVTV
4z4dO0XIQGtGdHDgZnH7JxkbyQjboUNPAgMBAAGjgdIwgc8wEgYDVR0TAQH/BAgw
BgEB/wIBADAOBgNVHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFAW17Y3FddasukIIfdaz
QW6Gsr3ZMGIGA1UdIwRbMFmAFC/cftTz002aAyJ84yIXbyVs3h2DoTakNDAyMSIw
IAYDVQQDDBlTZWxmLXNpZ25lZCBsb2NhbCBDQSBSb290MQwwCgYDVQQLDANEZXaC
CQD/HOKbSjsljjAmBgNVHR4EHzAdoBswDIIKLmxvY2FsaG9zdDALgglsb2NhbGhv
c3QwDQYJKoZIhvcNAQELBQADggEBAHKVWkayKBRTAJGMC7k+0o0pDOME4FraiEDb
l7/khNRSZDlhFmG0dgZOno1sQQcbU8LHAsV3L66TUnBPMN7n9rqzFt5x6EAlBNma
sqFYjwqcO+BO3CX/2Z/DiqWxNVFacWWZmqJX8nZlg2J6KFKkr1Mv2e8hoHGRNRbp
Amp8d3+Ln4IepBjBrzIJgl7dwysYTNvJorZ5Lgh5UQVqymGeuMXwTUGuezxs9YRr
jgu9fMseKjd6TdSO+6m93ohnfzHbeDvBSuorvanBLmdWYIpvaqBKTbK6oAj9bNBy
2GETlB2RY059lwPmqSemHldg4xy6Vxoy2HOI2fT0TzxsPgIf7xA=
-----END CERTIFICATE-----""",
    ],
    certificate="""-----BEGIN CERTIFICATE-----
MIIC5zCCAc+gAwIBAgIBAjANBgkqhkiG9w0BAQsFADAyMSIwIAYDVQQDDBlTZWxm
LXNpZ25lZCBsb2NhbCBDQSBSb290MQwwCgYDVQQLDANEZXYwHhcNMTkwNTE1MDkx
NjE1WhcNMjkwNTEyMDkxNjE1WjAiMRIwEAYDVQQDDAlsb2NhbGhvc3QxDDAKBgNV
BAsMA0RldjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOZrlKi88RoE
EL7YWQegtzPzUWhtdKPoP+uNCVh0e8dR5d8Cltn0AwJsv7QEHtfnP4RicqoTVRCO
GlfWKFd0WLG9ZA9BUoaN5FZv7AibAzWpdqiUMiabi1Jqbdtuo7CTdTRNuxIE2akW
gBJsuf8Pu/uukaiZjPLXoKJ2pOzsJKH0JOjYx19/UdSu+XbvHdjY27/cY/HYTqe5
EkW86CLA9/T6wFO6epLotEWiLyCA/MVck6FJUmpOOAW65seVe39xQqbv1rFT2IUJ
75mKwMNGHQYxFnWxSASClavGzem3sv4OCBzEctr5LqT//rHC8QG+Hbck7VlIFDp5
EnS5OKuVnP0CAwEAAaMYMBYwFAYDVR0RBA0wC4IJbG9jYWxob3N0MA0GCSqGSIb3
DQEBCwUAA4IBAQB1HH/z9Pk5d1dDdkjJllHQgA6kUTEVeYCetgqS8hcPx3RXSlZN
cNPns84GhsgVEHyF6vLjFwoYPzj2Wt9+50lCgDeIXuibWOnRvKHzNKuNvZ9PnBKI
7iaDi72i1p2wdjV1kGL+VkAWg7H/MRzWptYxSI7KjB5QVQUGmxW6VqUy6IFP2prm
Gen+J9WhkA0T6n0LvAbJJu7lgYU/OTShgeMiVBULTxRWTD/iSpqnfOFk7f7XTI+R
KFix+WBELV/8kcUiy961olDNKq58TGLC+moXQfnLKC/d6H2tttCpgpTVxcbd6a6F
mE/ob1G3JUEheV/dQMp6yESTmPgEY2BicuUY
-----END CERTIFICATE-----
""",
    key="""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDma5SovPEaBBC+
2FkHoLcz81FobXSj6D/rjQlYdHvHUeXfApbZ9AMCbL+0BB7X5z+EYnKqE1UQjhpX
1ihXdFixvWQPQVKGjeRWb+wImwM1qXaolDImm4tSam3bbqOwk3U0TbsSBNmpFoAS
bLn/D7v7rpGomYzy16CidqTs7CSh9CTo2Mdff1HUrvl27x3Y2Nu/3GPx2E6nuRJF
vOgiwPf0+sBTunqS6LRFoi8ggPzFXJOhSVJqTjgFuubHlXt/cUKm79axU9iFCe+Z
isDDRh0GMRZ1sUgEgpWrxs3pt7L+DggcxHLa+S6k//6xwvEBvh23JO1ZSBQ6eRJ0
uTirlZz9AgMBAAECggEAL9VjfggDMTho1YWKLegyQAmh+8DFNwWOx3J23zMHQyCA
TOR3tnVObqFuxosYcA+kgvIBBcePoCkv1M4zf7w6cWN0syoHXMF2Bm+jm0G6z9gH
NwXUx2kA6jIH7kawmoZyDVKZpCr3mH+ARNLnZci5aI0b1dlShlM3GKLyp/B5xljI
u+ClS6B9RKG0eLvEnKVlSWKiQx8jiRe4seA/jXNi/4a6nxYXvY4QJQPDhAERm6ep
GYPc5OOxzSAMyTh3srqkqUkg/2VTDuh6qGORmMqx65uKf5/M15hD81UJx5VLcMYn
s8vN49MoqKx2X8kzqKbbd8to8lU+bt0/IYGsiygfwQKBgQD1+KnhlXf3wcNNqvfo
cGts5kDTBUr3om+z7Wq7RUMb+W82j1EHTcaqKbm+O+Il6GhVSmbW4hCdoPxWbTfk
/T/22j+0MKHFlGOQzRR58+oDd9ZM2sQk1yGLIbI5nPvvkikqu8R/bHsL9Bn5TUUQ
XOFSPp/XuWuQLiLXKze2JwNYrQKBgQDv0JoOEgZui0p8bVUY1iWhTS5JLk8Bxuxr
IQny9A3MRbmsd/JTWEq+11K53kStalF3Myvlsz6MvG6+1//ThvJdsgwy+ef5m8bf
8Id5qh2/Owt5N66QOxz4oi9HKKRMcVbw37OK5LxCRLgzo5xQfiDQifvlvbNxjKdB
ifTazv9PkQKBgQCNYMkcTVIwSOHd8YgexQcqB8p4wBEP9wCnda4kR7JEEQHYZVXY
kd6/jc4iRr88tLHLXEFx/2w3fgGsF4jKCLpMQ7Pb+RvyudDkuMutMQJvzeCSOigF
WNYB53NOZCn20Jby5gwShaLQAxUu0zgAKLKmGDK9xujJbYs/C6sw+omU3QKBgH5R
+iP5OKwX8PdTu+RmQNITTpM7smA0QSo47/2qsm3sOF5xnBJsyop171x6iOBzxU+t
g6zt2r/VLdyW+GmahqX1+FkNrDSd6obhMutSQXMOjf+e5fORP7Rz8cVg0hJ2DR66
Jt+9lrCtc/23a8o2deCDHk2ovBHOzfdGzNRI/tERAoGBALaVapcbIWmd3wV+Ua9U
0ALcjbh8kZZC7fjVuuN6afD5J/Oayms/dZUZGBuL3CcDaU9y/dTKON2K3RoF/X75
/IUtyiswmkxXs5yk6CeqxxJmjACh8Gfp2fSJHpz654EqSrgZvoNM/xQbn2t65uE4
rcKh6J5XzhXswduHGcBZwgzO
-----END PRIVATE KEY-----
""",
)
