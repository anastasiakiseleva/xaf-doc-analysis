---
uid: DevExpress.ExpressApp.Model.IModelApplication.AboutInfoString
name: AboutInfoString
type: Property
summary: Specifies summary information on the current application that is intended to be shown in the "About" informational block.
syntax:
  content: |-
    [DefaultValue("{0:ProductName}<br>{0:Version}<br>{0:Copyright}<br>{0:Description}")]
    string AboutInfoString { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that is summary information on the current application.
seealso:
- linkId: "113445"
---
The `AboutInfoString` property can be set to any string. This string accepts the following format items: {0:ProductName}, {0:Version}, {0:Copyright}, {0:Company} and {0:Description}. HTML tags are also supported (see [How to: Apply HTML Formatting to Windows Forms XAF UI Elements](xref:113130)). By default, the following value is set: _{0:ProductName}\<br>{0:Version}\<br>\<br>{0:Copyright}\<br>\<br>{0:Company}\<br>\<br>{0:Description}_.

The [](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController) uses this property to set the [](xref:DevExpress.ExpressApp.SystemModule.AboutInfo) object's [AboutInfo.AboutInfoString](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString) property, if the latter has not been already set to another value in code.

For details on displaying the value set to this property in the "About" informational block, refer to the following topics:
* [AboutInfo.AboutInfoString](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString)
* [](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController)