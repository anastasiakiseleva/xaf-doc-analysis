---
uid: DevExpress.ExpressApp.Model.IModelLayoutElementWithCaptionOptions.CaptionLocation
name: CaptionLocation
type: Property
summary: Specifies a layout element's caption location.
syntax:
  content: Locations CaptionLocation { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.Locations
    description: A **DevExpress.Persistent.Base.Locations** enumeration value specifying a layout element's caption location.
seealso: []
---
The following values are available:

* **Bottom** - the caption is located at the bottom.
* **Default** - the caption is located at the top (the default setting).
* **Left** - the caption is located on the left.
* **Right** - the caption is located on the right.
* **Top** - the caption is located at the top.

In XAF ASP.NET Core Blazor UI applications, the following values are available:

* **Top** - the caption is located at the top. If the value is set to **Bottom**, the caption is displayed at the top.
* **Left** - the caption is located on the left. If the value is set to **Right**, the caption is displayed on the left.
* **Default** - the caption is located at the top (the default setting).

In XAF ASP.NET Core Blazor UI applications, the **CaptionLocation** property affects only layout items and does not affect layout groups and layout tabs.