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
    description: A layout element's caption location.
seealso: []
---
In XAF ASP.NET Core Blazor UI applications, the `CaptionLocation` property has the following limitations:
* An application can display a caption in two positions: above an item or to its left.
* The `CaptionLocation` property affects only layout items and does not affect layout groups and layout tabs.
* If viewport sizes are less than 768 px, captions are displayed above the associated editors regardless of the `CaptionLocation` property value.