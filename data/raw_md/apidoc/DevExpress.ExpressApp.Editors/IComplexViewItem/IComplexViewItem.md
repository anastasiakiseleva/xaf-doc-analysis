---
uid: DevExpress.ExpressApp.Editors.IComplexViewItem
name: IComplexViewItem
type: Interface
summary: Declares members implemented by [View Items](xref:112612) that have access to the [](xref:DevExpress.ExpressApp.XafApplication) object and [](xref:DevExpress.ExpressApp.IObjectSpace) of the current [View](xref:112611).
syntax:
  content: public interface IComplexViewItem
seealso:
- linkId: DevExpress.ExpressApp.Editors.IComplexViewItem._members
  altText: IComplexViewItem Members
- linkId: DevExpress.ExpressApp.XafApplication
- linkId: DevExpress.ExpressApp.BaseObjectSpace
- linkId: DevExpress.ExpressApp.Editors.IComplexListEditor
---
When implementing a [custom Property Editor](xref:113097) or [custom View Item](xref:405483), you may want to:

* Load arbitrary data from the application database
* Use methods provided by the application object (for instance, [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*))

In these scenarios, a View Item or Property Editor requires access to the application object and to the Object Space of the current View. To get these objects, the Property Editor should support the **IComplexViewItem** interface. This interface exposes a single [IComplexViewItem.Setup](xref:DevExpress.ExpressApp.Editors.IComplexViewItem.Setup(DevExpress.ExpressApp.IObjectSpace,DevExpress.ExpressApp.XafApplication)) method that accepts _objectSpace_ and _application_ parameters. This method is called automatically for all **IComplexViewItem** View Items when a View is shown.

Here is an example of how to implement **IComplexViewItem** in a [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) descendant:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
// ...
public class CustomPropertyEditor : PropertyEditor, IComplexViewItem {
    private IObjectSpace objectSpace;
    private XafApplication application;

    #region IComplexViewItem Members
    void IComplexViewItem.Setup(IObjectSpace objectSpace, 
XafApplication application) {
        this.objectSpace = objectSpace;
        this.application = application;
    }
    #endregion

    // Example:
    protected override object CreateControlCore() {
        IList dataSource = objectSpace.GetObjects(Model.ModelMember.Type);
        // ...
    }
}
```
***

[!example[XAF WinForms - How to use a custom Lookup Property Editor control for reference properties](https://github.com/DevExpress-Examples/obsolete-xaf-win-custom-lookup-property-editor)]