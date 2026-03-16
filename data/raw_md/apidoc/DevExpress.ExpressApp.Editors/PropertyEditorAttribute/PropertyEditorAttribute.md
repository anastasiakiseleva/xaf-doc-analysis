---
uid: DevExpress.ExpressApp.Editors.PropertyEditorAttribute
name: PropertyEditorAttribute
type: Class
summary: Registers a custom [Property Editor](xref:113097) in the [Application Model](xref:112580).
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class, Inherited = false, AllowMultiple = true)]
    public sealed class PropertyEditorAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Editors.PropertyEditorAttribute._members
  altText: PropertyEditorAttribute Members
---
When a XAF application loads, the reflection mechanism locates classes with the `PropertyEditor` attribute. The [Application Model](xref:112580) includes these classes into its [Property Editor](xref:113097) collection. The attribute's parameter specifies the target object type for the **List Editor**.

When you register a Property Editor you can specify a class or an interface as the target type. Editors associated with interfaces have higher priority.

> [!tip]
> Use the @DevExpress.ExpressApp.Editors.ListEditorAttribute to register and use a custom [List Editor](xref:113189).

The `PropertyEditor` attribute includes the following parameters:

`propertyType`
:   Specifies the associated property type. Set this parameter to @System.Object to support properties of any type.
`isDefaultEditor`
:   Specify `true` to use this Property Editor as the default choice for specified property types. Otherwise, this Property Editor is available in the Model Editor, but you must explicitly assign it to types or Detail View Items.
`alias`
:   Sets an alias for the Property Editor.


### Use Your Custom Class as the Default Property Editor

You can specify the default Property Editor in the following two ways:

In code
:   Apply `PropertyEditorAttribute` to your custom Property Editor class. Pass @System.Object and `true` as attribute parameters.

    ```csharp
    // Set the  CustomPropertyEditor as default Property Editor
    [PropertyEditor(typeof(object), true)]
    public class CustomPropertyEditor : BlazorPropertyEditorBase { /* ... */ }
    ```

In the Model Editor
:   Use `PropertyEditorAttribute` to register the custom Property Editor in the Application Model. Pass @System.Object and `false` as attribute parameters.

    ```csharp
    // Register CustomPropertyEditor as an accessible Property Editor for properties of any type
    [PropertyEditor(typeof(object), false)]
    public class CustomPropertyEditor : BlazorPropertyEditorBase { /* ... */ }
    ```

    Open the Model Editor and select **ViewItems | PropertyEditors**. Set the @DevExpress.ExpressApp.Editors.IModelRegisteredViewItem.DefaultItemType property to your editor class name.

    ![DefaultItemType property in the Model Editor](~/images/xaf-custom-property-editor-model-editor-default.png)

### Assign Your Custom Property Editor to Properties of a Specific Type

You can associate a Property Editor with a specific data type using two ways:

In code
:   Apply `PropertyEditorAttribute` to your editor class. Pass the required data type and `true` as attribute parameters.

    ```csharp
    // Assign CustomDateTimePE to DateTime properties
    [PropertyEditor(typeof(DateTime), true)]
    public class CustomDateTimePE : BlazorPropertyEditorBase { /*...*/ }
    ```

In the Model Editor
:   Use `PropertyEditorAttribute` to register the custom Property Editor in the Application Model. Pass the required data type and `false` as attribute parameters.

    ```csharp
    // Register CustomDateTimePE as an accessible property editor for DateTime properties
    [PropertyEditor(typeof(DateTime), false)]
    // Or Register CustomDateTimePE as an accessible property editor for properties of any type
    //[PropertyEditor(typeof(object), false)]
    public class CustomDateTimePE : BlazorPropertyEditorBase { /*...*/ }
    ```

    Open the Model Editor and select **ViewItems | PropertyEditors | {Property Type}**. Set the @DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.EditorType property to your editor class name.

    ![EditorType property in the Model Editor](~/images/xaf-custom-property-editor-model-editor-type.png)

### Assign Your Custom Property Editor to a Specific Property

Use `PropertyEditorAttribute` to register the custom Property Editor in the Application Model. Pass the target data type as the first parameter, and set the second parameter to `false`.

```csharp
// Register CustomStringPE as available property editor for string properties
[PropertyEditor(typeof(string), false)]
public class CustomStringPE : BlazorPropertyEditorBase { /*...*/ }
```

Open the Model Editor and select **BOModel | {MySolution}.Module.BusinessObjects | {ClassName} | OwnMembers | {PropertyName}**. Set the @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType property to your editor class name.

![PropertyEditorType property in the Model Editor](~/images/xaf-custom-property-editor-model-editor-property.png)

### Assign Your Custom Property Editor to a Detail View Item

Register the editor in code as demonstrated in the previous section. In the Model Editor, select **Views | {MySolution}.Module.BusinessObjects | {ClassName} | {ClassName}_DetailView | Items | {PropertyName}**. Set the @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType property to your editor class name.

![PropertyEditorType property in the Model Editor](~/images/xaf-custom-property-editor-model-editor-view-item.png)


### Use Your Custom Property Editor with Protected Properties

To assign a Property Editor to protected properties, implement the `IProtectedContentEditor` interface in your editor class. In `PropertyEditorAttribute`, set `propertyType` to @System.Object and `isDefaultEditor` to `true`.

```csharp
// Assign CustomProtectedContentPE to protected properties
[PropertyEditor(typeof(object), true)]
public class CustomProtectedContentPE : BlazorPropertyEditorBase, IProtectedContentEditor { /* ... */ }
```
You can set `isDefaultEditor` to `false` and use the Model Editor to specify the target type or property. Select **ViewItem | PropertyEditors** and set the @DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditors.ProtectedContentPropertyEditor property to your editor class name.

### Property Editor Alias

Property Editors are usually platform-specific, and you have to register each Property Editor separately for every platform you support. 

You can set the same alias for both WinForms and ASP.NET Core Blazor editors, and use this alias to refer to your editor in platform-independent code. The application automatically chooses the correct editor version for the current platform.

Specify the `alias` parameter in `PropertyEditorAttribute`:

# [C# (Blazor)](#tab/tabid-blazor)
 
```csharp
[PropertyEditor(typeof(string), "CustomStringPEAlias ", false)]
public class CustomBlazorStringPE : BlazorPropertyEditorBase { /* ... */}
```
 
# [C# (WinForms)](#tab/tabid-win)
 
```csharp
[PropertyEditor(typeof(string),"CustomStringPEAlias", false)]
public class CustomWinStringPE : DXPropertyEditor { /* ... */}
```
 
***

Use @DevExpress.Persistent.Base.EditorAliasAttribute to assign the editor alias to a property.

```csharp
[EditorAlias("CustomStringPEAlias")]
public virtual String FirstName { get; set; }
```

You can also call the @DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterPropertyEditorAlias* method to register your editor's alias.

### Use Your Custom Class as a Lookup Property Editor

The default Lookup Property Editor uses a [predefined alias](xref:DevExpress.ExpressApp.Editors.EditorAliases._members): `LookupPropertyEditor`. To replace the default editor, use this alias as a `PropertyEditorAttribute` parameter.

```csharp
[PropertyEditor(typeof(object), EditorAliases.LookupPropertyEditor, true)]
public class CustomLookupPropertyEditor : BlazorPropertyEditorBase { /* ... */ }
```

[!example[XAF WinForms - How to use a custom Lookup Property Editor control for reference properties](https://github.com/DevExpress-Examples/obsolete-xaf-win-custom-lookup-property-editor)]

### Alternative Property Editor Registration Method (No Attributes)

You can disable the mechanism that locates classes decorated with `PropertyEditorAttribute`. This change may help you optimize application load time. 

To activate manual List Editor registration, override the `ModelBase.RegisterEditorDescriptors` method. Call the @DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterPropertyEditor* method to register required List Editors:

```csharp
public class CustomStringPE : BlazorPropertyEditorBase { /* ... */ }
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
            editorDescriptorsFactory.RegisterPropertyEditor(typeof(String), typeof(CustomStringPE), true);
        }
        //...
    }
    // ...
}
```
***

Refer to the @DevExpress.ExpressApp.ModuleBase property description for details.

## Examples

* <xref:402189>
* <xref:112679>