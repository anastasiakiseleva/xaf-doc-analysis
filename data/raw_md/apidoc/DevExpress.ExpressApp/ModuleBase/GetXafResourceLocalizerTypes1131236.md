---
uid: DevExpress.ExpressApp.ModuleBase.GetXafResourceLocalizerTypes
name: GetXafResourceLocalizerTypes()
type: Method
summary: Returns a collection of Resource Localizer types that can be used in an application that uses the current module.
syntax:
  content: public virtual ICollection<Type> GetXafResourceLocalizerTypes()
  return:
    type: System.Collections.Generic.ICollection{System.Type}
    description: An **ICollection\<Type>** collection containing the types of the Resource Localizers to be supplied with the current module.
seealso: []
---
Each Developer Express component or library has a specific Localizer class (see the table below) that provides localized strings for this component/library. If your distributable module uses a control from one of the DevExpress libraries, you can supply a Resource Localizer with the module. In this instance, the control's resources can be localized via the [](xref:DevExpress.ExpressApp.Model.IModelLocalization) node in the [Model Editor](xref:112830) in any application that uses your module. To introduce a Resource Localizer, inherit it from a corresponding **Localizer** class and implement the **IXafResourceLocalizer** interface. All the necessary DevExpress localizers are listed in the [Localizing WinForms Controls via Localizer Objects](xref:1866) document. To learn how to implement the **IXafResourceLocalizer** interface, see the **XAF** sources.

To register a custom Resource Localizer in your module, override the **GetXafResourceLocalizerTypes** method. See an example:

# [C#](#tab/tabid-csharp)

```csharp
public class Module : ModuleBase {
   public override ICollection<Type> GetXafResourceLocalizerTypes() {
     ICollection<Type> result = new List<Type>();
      result.Add(typeof(GridControlLocalizer));
      result.Add(typeof(LayoutControlLocalizer));
      return result;
   }
   //...
}
```
***
