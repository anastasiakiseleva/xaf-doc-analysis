---
uid: "403861"
title: Access Object Space, Security System, and Caption Helper in Custom Endpoint Methods
owner: Yekaterina Kiseleva
seealso:
  - linkId: "403858"
  - linkId: "403669"
---
# Access Object Space, Security System, and Caption Helper in Custom Endpoint Methods

This topic describes how to access an [Object Space](xref:113711), the [Security System](xref:113366), and the [Caption Helper](xref:113298) from custom endpoint methods.

## Useful APIs

{|
|-
! Object to access
! Injecting service
! Methods and properties
|-

| [Object Space](xref:113707)
| @DevExpress.ExpressApp.IObjectSpaceFactory  
@DevExpress.ExpressApp.INonSecuredObjectSpaceFactory
| [IObjectSpaceFactory.CreateObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceFactory.CreateObjectSpace(System.Type))  
[INonSecuredObjectSpaceFactory.CreateObjectSpace](xref:DevExpress.ExpressApp.INonSecuredObjectSpaceFactory.CreateNonSecuredObjectSpace(System.Type))
|-

| [Security System](xref:113366)
| @DevExpress.ExpressApp.Security.ISecurityProvider  
@DevExpress.ExpressApp.Security.ISecurityStrategyBase
| [ISecurityProvider.GetSecurity](xref:DevExpress.ExpressApp.Security.ISecurityProvider.GetSecurity)  
[ISecurityStrategyBase.IsAuthenticated](xref:DevExpress.ExpressApp.Security.ISecurityStrategyBase.IsAuthenticated)  
[ISecurityStrategyBase.User](xref:DevExpress.ExpressApp.Security.ISecurityStrategyBase.User)
|-

| [Caption Helper](xref:DevExpress.ExpressApp.Utils.CaptionHelper)
| @DevExpress.ExpressApp.Services.Localization.ICaptionHelperProvider
| [ICaptionHelperProvider.GetCaptionHelper](xref:DevExpress.ExpressApp.Services.Localization.ICaptionHelperProvider.GetCaptionHelper)
|}

[!include[<access-object-space-in-custom-endpoint><access-security-system-in-custom-endpoint><access-caption-helper-in-custom-endpoint>](~/templates/access-object-space-security-and-caption-helper-in-asp-net-core.md)]
