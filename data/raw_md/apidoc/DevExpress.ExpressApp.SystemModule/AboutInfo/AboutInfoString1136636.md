---
uid: DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString
name: AboutInfoString
type: Property
summary: Specifies summary information on the current application that is intended to be shown in the "About" informational block.
syntax:
  content: public string AboutInfoString { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that is summary information on the current application.
seealso: []
---
You can set `AboutInfoString` property to any string. This string accepts the following format items: `{0:ProductName}`, `{0:Version}`, `{0:Copyright}`, `{0:Company}`, and `{0:Description}`. XAF replaces them with the corresponding property values of the `AboutInfo` object. HTML tags are also supported (see [How to: Apply HTML Formatting to Windows Forms XAF UI Elements](xref:113130)).

The [](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController) sets this property to the value of the Application node's `AboutInfoString` property, before showing the "About" informational block in a UI. By default, the following value is set in the Application Model: _{0:ProductName}\<br>{0:Version}\<br>\<br>{0:Copyright}\<br>\<br>{0:Company}\<br>\<br>{0:Description}_.

You can customize the `AboutInfoString` property value in any of the following ways:

* Assign the required value to the `AboutInfoString` property of the **Application** node.
* If the `AboutInfoString` property's default value is appropriate, but its format item values are invalid, set the `ProductName`, `Version`, `Copyright`, `Company` and `Description` properties of the Application node to the required values.
* Set the required values for the properties of the `AboutInfo` object in code:
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    using System;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.SystemModule;
    //...
    public class MyController : WindowController {
        protected override void OnActivated() {
            base.OnActivated();
            AboutInfo.Instance.ProductName = "New Product";
        }
    }
    ```
    ***
    
    The values that are set in code override the default values from the Application Model.
