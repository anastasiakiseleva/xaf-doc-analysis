---
uid: "112655"
seealso:
- linkId: DevExpress.ExpressApp.Utils.CaptionHelper
title: 'How to: Localize Custom String Constants'
owner: Ekaterina Kiseleva
---
# How to: Localize Custom String Constants

This topic demonstrates how to localize custom strings. This example uses confirmation messages. The [Application Model](xref:112580) has the **Localization** node that allows [localization](xref:112595) of various constants. You can use this node to localize custom strings used in your applications.

For instance, a feature that you implement in your application uses the following code:

# [C#](#tab/tabid-csharp)

```csharp
using System.Windows.Forms;
// ...
if (MessageBox.Show("Do you wish to cancel your changes?", "", MessageBoxButtons.YesNo) 
   == DialogResult.Yes) {
   // ...
}
```
***

To localize custom strings from the WebApi context, refer to the following article: [Access Caption Helper in Custom Endpoint Methods](xref:403861).

## Add Localization Items in the Model Editor

To localize the text of the confirmation message above, add the **LocalizationItem** child node to the **Localization** | **Messages** node, and specify its **Value** property in the required language:

![LocalizeCustomConstants_ModelEditor3](~/images/localizecustomconstants_modeleditor3116882.png)

You can use the static [CaptionHelper.GetLocalizedText](xref:DevExpress.ExpressApp.Utils.CaptionHelper.GetLocalizedText*) method to get the required message text from the new node.

# [C#](#tab/tabid-csharp)

```csharp
using System.Windows.Forms;
using DevExpress.ExpressApp.Utils;
// ...
if (MessageBox.Show(CaptionHelper.GetLocalizedText("Messages", "DoYouWishToCancelChanges"), 
    "", MessageBoxButtons.YesNo) == DialogResult.Yes) {
    // ...
}
```
***

If you need to localize multiple custom strings, add the **LocalizationGroup** node to the **Localization** node and specify your strings there. In this example, this node is called **Confirmations**:

![LocalizeCustomConstants_ModelEditor2](~/images/localizecustomconstants_modeleditor2116881.png)

# [C#](#tab/tabid-csharp)

```csharp
using System.Windows.Forms;
using DevExpress.ExpressApp.Utils;
// ...
if (MessageBox.Show(CaptionHelper.GetLocalizedText(
    @"Messages\Confirmations", "DoYouWishToCancelChanges"), 
        "", MessageBoxButtons.YesNo) == DialogResult.Yes) {
    // ...
}
```
***

The **LocalizationGroup** node can have a multilevel structure. You can use the **CaptionHelper.GetLocalizedText** method to create a complex hierarchy. This method accepts a path as an input parameter. For instance, to access the **Localization** | **Messages** | **Confirmations** | **DataChangingConfirmations** group, use the "Messages\Confirmations\DataChangingConfirmations" path. Do not include the **Localization** node itself in the path.

## Export Localization Items from Resource Files

You can add Localization Items from a resource file. Assume you have the following _MyResource.resx_ resource file in your XAF solution:

![LocalizeCustomConstants_ResourceFile](~/images/localizecustomconstants_resourcefile116878.png)

To export values from this file to the Application Model, implement a Resource Localizer (**XafResourceLocalizer** descendant):

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Localization;
// ...
public class MyXafResourceLocalizer : XafResourceLocalizer {
    protected override IXafResourceManagerParameters GetXafResourceManagerParameters() {
        string[] localizationGroupPath = new string[] { "Messages", "Confirmations" };
        return new XafResourceManagerParameters(localizationGroupPath, 
            "MySolution.Module.MyResource", "", GetType().Assembly);
    }
}
```
***

In this snippet, "MySolution.Module.MyResource" is the resource name. Items from this resource are added to the **Localization** | **Messages** | **Confirmations** Localization Group. Add the Resource Localizer type to the [ModuleBase.ResourcesExportedToModel](xref:DevExpress.ExpressApp.ModuleBase.ResourcesExportedToModel) collection to register the Resource Localizer in a module.

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        // ...
        ResourcesExportedToModel.Add(typeof(MyXafResourceLocalizer));
    }
    // ...
}
```
***

Alternatively, you can register a resource localizer in the overridden [ModuleBase.GetXafResourceLocalizerTypes](xref:DevExpress.ExpressApp.ModuleBase.GetXafResourceLocalizerTypes) method.

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class ResourceLocalizerModule : ModuleBase {
    // ...
    public override ICollection<Type> GetXafResourceLocalizerTypes() {
        ICollection<Type> localizers = base.GetXafResourceLocalizerTypes();
        localizers.Add(typeof(MyXafResourceLocalizer));
        return localizers;
    }
}
```
***

In this instance, you can add or remove a localizer in the Application Designer.

![LocalizeCustomConstants_ResourcesExportedToModel](~/images/localizecustomconstants_resourcesexportedtomodel116880.png)

Rebuild the solution and invoke the Model Editor. You can see that items from the _MyResource.resx_ resource are exported to the Application Model.

![LocalizeCustomConstants_ModelEditor](~/images/localizecustomconstants_modeleditor116879.png)

You can now use the [CaptionHelper.GetLocalizedText](xref:DevExpress.ExpressApp.Utils.CaptionHelper.GetLocalizedText*) method to access localizable values from code.
