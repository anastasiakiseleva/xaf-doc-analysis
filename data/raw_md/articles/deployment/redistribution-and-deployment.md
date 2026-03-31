---
uid: "113033"
seealso: []
title: Redistribution and Deployment
---
# Redistribution and Deployment

XAF applications and referenced assemblies should be deployed at the same time. Multiple Developer Express assemblies are considered redistributable under the [End User License Agreement](xref:2218) (EULA) and can be distributed to your application's end-users. You must have a valid license to legally distribute applications that use Developer Express components.

It is not necessary to deploy all the listed redistributable files with your application. Refer to the [Deployment Tutorial](xref:112691#deployment-tutorial----lessons) to learn how to correctly deploy XAF applications with the required assemblies.

All the DevExpress assemblies your XAF Application requires and references are available as part of the Universal Subscription.

> [!IMPORTANT]
> Consult the [End User License Agreement](xref:2218) (EULA) for additional up-to-date information on redistributable assemblies, tools, and executables.


## Other Redistributable DevExpress Assemblies

In addition to the files listed in the EULA, an XAF application may require you to distribute other Developer Express assemblies supplied with installation. This list depends on DevExpress controls employed in an application.

> [!NOTE]
> Use the [Assembly Deployment Tool](xref:17237) to analyze your project and to obtain the list of assemblies you should deploy. Compare the assemblies identified by this tool identifies to redistributable assemblies available in the [End User License Agreement](xref:2218) (EULA).

The following is a list of links to redistributable assemblies grouped according to specific application needs:

* [WinForms and Cross-Platform applications](xref:15031)
* [Dashboards for WinForms applications](xref:12135)
* [Reports for WinForms](xref:15322)

## Non-Redistributable Files

The following table lists Developer Express libraries where distribution is strictly prohibited:

1. Design-time libraries where names end with ".Design".
2. Tools in the _[!include[PathToXafTools](~/templates/path-to-xaf-tools.md)]_ folder, except for those listed in the previous sections.

> [!IMPORTANT]
> You cannot use the [DevExpress .NET Products Installer](xref:15655) to deploy assemblies onto an end-user machine; you should manually deploy necessary assembly files onto the target machine instead.
