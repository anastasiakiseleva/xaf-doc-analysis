---
uid: "118084"
seealso:
- linkId: "116666"
- linkType: HRef
  linkId: https://learn.microsoft.com/en-us/windows/desktop/hidpi/high-dpi-desktop-application-development-on-windows
  altText: Writing DPI-Aware Desktop and Win32 Applications
title: 'High DPI Support in a Windows Forms Application'
owner: Ekaterina Kiseleva
---
# High DPI Support in a Windows Forms Application

Before you run an XAF Windows Forms application in a high-DPI environment, ensure that the application is DPI-aware.

To ensure that an application has proper high DPI support, the [Template Kit](xref:405447) adds the following application settings section to the _YourApplicationName.Win\App.config_ file every time you create a new project:
    
```XML
<applicationSettings>
  <DevExpress.LookAndFeel.Design.AppSettings>
    <setting name="DPIAwarenessMode" serializeAs="String">
      <value>System</value>
    </setting>
  </DevExpress.LookAndFeel.Design.AppSettings>
</applicationSettings>
```

To enable DPI-Aware mode manually, use one of the techniques described in the following topic: [High DPI Support](xref:116666).

## SVG Images

All applications created with the [Template Kit](xref:405447) support SVG images.

To enable support for SVG images manually, go to the _Program.cs_ file. In the `Main` method call, set the [](xref:DevExpress.ExpressApp.Utils.ImageLoader.UseSvgImages) property to `true`.

## Current Limitations and Recommendations

* Design your applications under 96 DPI (100%). When you downscale a form developed in a high-DPI environment, issues may occur.
* XAF does not support [Per-Monitor DPI](https://learn.microsoft.com/en-us/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows#per-monitor-and-per-monitor-v2-dpi-awareness). When you drag an application window between monitors with different DPI settings, the operating system uses its built-in mechanisms to scale the window accordingly.
