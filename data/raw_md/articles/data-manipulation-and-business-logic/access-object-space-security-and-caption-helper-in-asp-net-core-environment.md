---
uid: "403669"
title: Access Object Space, Security System, and Caption Helper in the ASP.NET Core Environment
owner: Dmitry Egorov
seealso:
  - linkId: '403861'
  - linkId: '114515'
---
# Access Object Space, Security System, and Caption Helper in the ASP.NET Core Environment

This topic describes how to access an [Object Space](xref:113711), the [Security System](xref:113366), the [Caption Helper](xref:113298), and [XAF Modules](xref:118046) from an ASP.NET Core service or middleware, Web API controllers, custom Razor pages, and components.

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
[INonSecuredObjectSpaceFactory.CreateNonSecuredObjectSpace](xref:DevExpress.ExpressApp.INonSecuredObjectSpaceFactory.CreateNonSecuredObjectSpace(System.Type))
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


[!include[<access-object-space-in-asp-net-core-environment><access-security-system-in-asp-net-core-environment><access-caption-helper-in-asp-net-core-environment>](~/templates/access-object-space-security-and-caption-helper-in-asp-net-core.md)]

