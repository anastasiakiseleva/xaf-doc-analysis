---
uid: DevExpress.Persistent.Base.ToolTipAttribute
name: ToolTipAttribute
type: Class
summary: Specifies a tooltip for a business object property in XAF WinForms and ASP.NET Core Blazor applications.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true, AllowMultiple = false)]
    public class ToolTipAttribute : ModelExportedValuesAttribute
seealso:
- linkId: DevExpress.Persistent.Base.ToolTipAttribute._members
  altText: ToolTipAttribute Members
---
The `ToolTipAttribute` class allows you specify tooltips for business object properties. Additionally, you can use the [Model Editor](xref:112582) to configure tooltips for the following elements:

* Business object properties
* Layout groups
* Navigation items and groups

The model uses [IModelToolTip.ToolTip](xref:DevExpress.ExpressApp.Model.IModelToolTip.ToolTip), [IModelToolTipOptions.ToolTipIconType](xref:DevExpress.ExpressApp.Model.IModelToolTipOptions.ToolTipIconType), and [IModelToolTipOptions.ToolTipTitle](xref:DevExpress.ExpressApp.Model.IModelToolTipOptions.ToolTipTitle) properties to specify tooltip settings.

### Set a Tooltip for a Business Object Property in Code

Use `ToolTipAttribute` to assign a tooltip to a class property. Once set for a class member, the tooltip is assigned for all related UI elements:

* Controls of Detail View items
* Layout groups
* Captions of layout items (not supported in Blazor applications)
* List View column headers in `GridListEditor` and `TreeListEditor` (WinForms), `DxGridListEditor` and `DxTreeListEditor` (ASP.NET Core Blazor)

# [C#](#tab/tabid-csharp)

```csharp
public class DemoTask : BaseObject {
    // ...
    [ToolTip("Provide a detailed task description.")]
    public virtual string Notes { get; set; }
    //...
}
```
***

![Property tooltip](~/images/xaf-ToolTipAttribute-property-tooltip.png)

### Set a Tooltip for a Business Object Property in the Model Editor

Select **BOModel | _\<ApplicationName>_.Module.BusinessObjects | _\<ClassName>_ | OwnMembers | _\<PropertyName>_** and specify a value for the `ToolTip` property.

![Property tooltip specified in model editor](~/images/xaf-ToolTipAttribute-property-tooltip-in-model-editor.png)

You can try this approach in the MainDemo application that is shipped with XAF and installed to the following default path: _[!include[PathToMainDemo](~/templates/path-to-main-demo-ef-core.md)]_.

### Set a Tooltip for a Layout Group in the Model Editor

Select **Views | _\<ApplicationName>_.Module.BusinessObjects | _\<ClassName>_ | _\<ClassName>_\_DetailView | Layout | _\<…>_ | _\<GroupName>_** and specify a value for the `ToolTip` property.

![Layout group tooltip](~/images/xaf-ToolTipAttribute-group-tooltip.png)

### Set a Tooltip for a Navigation Item or Group in the Model Editor

Select **NavigationItems | Items | _\<…>_ | _\<GroupOrItemName>_** and specify a value for the `ToolTip` property.

![Navigation item tooltip](~/images/xaf-ToolTipAttribute-navigation-tooltip.png)

### Limitations
* @DevExpress.Persistent.Base.ToolTipAttribute.ToolTipTitle and @DevExpress.Persistent.Base.ToolTipAttribute.ToolTipIconType properties are in effect in Detail Views of XAF Windows Forms applications only.
* In Blazor applications, tooltips for layout item captions are not supported.
* In Windows Forms applications, tooltips for navigation groups with [Outlook Style](xref:113198#navigation-bar-with-outlook-style) are not supported.
