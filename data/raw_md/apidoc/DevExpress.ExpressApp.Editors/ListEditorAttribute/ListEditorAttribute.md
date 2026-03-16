---
uid: DevExpress.ExpressApp.Editors.ListEditorAttribute
name: ListEditorAttribute
type: Class
summary: Registers a custom [List Editor](xref:113189) in the [Application Model](xref:112580).
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class, Inherited = false, AllowMultiple = true)]
    public class ListEditorAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Editors.ListEditorAttribute._members
  altText: ListEditorAttribute Members
---
When an XAF application loads, the reflection mechanism locates classes with the `ListEditor` attribute. The [Application Model](xref:112580) includes these classes into its [List Editor](xref:113189) collection. The attribute's parameter specifies the target object type for the **List Editor**.

> [!tip]
> Use the @DevExpress.ExpressApp.Editors.PropertyEditorAttribute to register a class as a [Property Editor](xref:113097).

The `ListEditor` attribute includes the following parameters:

`listElementType`
:   Sets the type of objects that the List Editor can display. Set this parameter to @System.Object to support objects of any type.
`isDefault`
:   Specify `true` to make this List Editor a default choice for the specified object type(s). Otherwise, the List Editor is available in the Model Editor, but you must explicitly assign it to an object type or a List View.

### Use Your Custom Class as the Default List Editor

You can specify the default List Editor in two ways:

In code
:   Apply `ListEditorAttribute` to your custom List Editor class. Pass @System.Object and `true` as attribute parameters.

    ```csharp
    // Set CustomListEditor as the default List Editor
    [ListEditor(typeof(object), true)]
    public class CustomListEditor : DxGridListEditor { /* ... */ }
    ```

In the Model Editor
:   Use `ListEditorAttribute` to register your custom List Editor in the Application Model. Pass @System.Object and `false` as attribute parameters.

    ```csharp
    // Register CustomListEditor as the available List Editor for properties of any type
    [ListEditor(typeof(object), false)]
    public class CustomListEditor : DxGridListEditor { /* ... */ }
    ```

    Open the Model Editor, select **Views**, and set the @DevExpress.ExpressApp.Model.IModelViews.DefaultListEditor property to your editor class name.

    ![DefaultListEditor property in the Model Editor](~/images/xaf-custom-list-editor-model-editor-default.png)

### Assign Your Custom List Editor to a Specific Object Type

You can link a custom List Editor to a specific type in the following two ways:

In code
:   Apply `ListEditorAttribute` to your editor class. Pass the required data type and `true` as attribute parameters.

    ```csharp
    // Assign CustomListEditor to Employee object type
    [ListEditor(typeof(Employee), true)]
    public class CustomListEditor : DxGridListEditor { /* ... */ }
    ```

In the Model Editor
:   Use `ListEditorAttribute` to register your custom List Editor in the Application Model. Pass the required data type and `false` as attribute parameters.

    ```csharp
    // Register CustomListEditor as the available list editor for Employee objects
    [ListEditor(typeof(Employee), false)]
    // Or Register CustomListEditor as the available List Editor for properties of any type
    //[ListEditor(typeof(object), false)]
    public class CustomListEditor : DxGridListEditor { /* ... */ }
    ```

    To assign this editor to a specific object type, open the Model Editor and select **BOModel | {MySolution}.Module.BusinessObjects | {ClassName}**. Set the @DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.EditorType property to your editor class name.

    ![EditorType property in the Model Editor](~/images/xaf-custom-list-editor-model-editor-type.png)

### Assign Your Custom List Editor to a List View Item

Register the editor in code as demonstrated in the previous section. In the Model Editor, select **Views | {MySolution}.Module.BusinessObjects | {ClassName} | {ClassName}_ListView**. Set the @DevExpress.ExpressApp.Model.IModelListView.EditorType property to your editor class name.

![EditorType property in the Model Editor](~/images/xaf-custom-list-editor-model-editor-list-view.png)

### Alternative List Editor Registration Method (No Attributes)

You can disable the mechanism that locates classes decorated with `ListEditorAttribute`. This change may help you optimize application load time. 

To activate manual List Editor registration, override the `ModelBase.RegisterEditorDescriptors` method. Call the @DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterListEditor* method to register required List Editors:


```csharp
public class CustomListEditor : DxGridListEditor { /* ... */ }
```

# [MySolution.Blazor.Server/BlazorModule.cs](#tab/tabid-csharp)
```csharp
using System.ComponentModel;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
using MySolution.Module.BusinessObjects;

namespace MySolution.Blazor.Server {
    public sealed class MySolutionBlazorModule : ModuleBase {
        protected override void RegisterEditorDescriptors(EditorDescriptorsFactory editorDescriptorsFactory) {
            editorDescriptorsFactory.RegisterListEditor(typeof(MyBusinessObject), typeof(CustomListEditor), true);
        }
        //...
    }
    // ...
}
```
***

Refer to the @DevExpress.ExpressApp.ModuleBase property description for details.

## Examples

* <xref:403258>
* <xref:112659>