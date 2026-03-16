---
uid: DevExpress.ExpressApp.Model.IModelLayoutManagerOptions.CaptionLocation
name: CaptionLocation
type: Property
summary: Specifies the default layout group and item caption location.
syntax:
  content: |-
    [DefaultValue(Locations.Default)]
    Locations CaptionLocation { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.Locations
    description: A **DevExpress.Persistent.Base.Locations** enumeration value specifying the default layout group and item caption location.
seealso:
- linkId: "112817"
---
The following values are available:

* **Bottom** - captions are located at the bottom.
* **Default** - captions are located at the top (the default setting).
* **Left** - captions are located at the left.
* **Right** - captions are located at the right.
* **Top** - captions are located at the top.

In XAF ASP.NET Core Blazor UI applications, the following values are available:

* **Top** - the caption is located at the top. If the value is set to **Bottom**, the caption is displayed at the top.
* **Left** - the caption is located on the left. If the value is set to **Right**, the caption is displayed on the left.
* **Default** - captions are located at the top (the default setting).

In XAF ASP.NET Core Blazor UI applications, the **CaptionLocation** property does not affect layout groups and tabbed groups.