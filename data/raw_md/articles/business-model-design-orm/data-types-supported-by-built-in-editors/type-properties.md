---
uid: "113579"
seealso:
- linkId: "402188"
title: Type Properties
---
# Type Properties

In XAF, properties of the `System.Type` type can be displayed in a combo box editor that lists the available object types in ASP.NET Core Blazor and WinForms applications.
 
 ## Examples
* [Type Properties in XPO](xref:113580)
* [Type Properties in EF Core](xref:113581)

## ASP.NET Core Blazor

![|XAF Type Properties ASP.NET Core Blazor, DevExpress](~/images/xaf-blazor-datatypeproperty-devexpress.png)

### TypePropertyEditor

[!include[typepropertyeditor](~/templates/typepropertyeditor.md)]

### VisibleInReportsTypePropertyEditor

The editor is inherited from `TypePropertyEditor`. Used by the [Reports V2 Module](xref:113591). It lists the types of business classes that have the `VisibleInReports` property of the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelClass) node set to `true`.

## WinForms

![XAF Type Properties WinForms](~/images/pe_typewin117361.png)

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

### TypePropertyEditor
	
Control: [](xref:DevExpress.XtraEditors.ImageComboBoxEdit) editor from the XtraEditors Library.
	
Repository Item: [](xref:DevExpress.XtraEditors.Repository.RepositoryItemImageComboBox) item from the XtraEditors Library.
	
Description:
	
[!include[typepropertyeditor](~/templates/typepropertyeditor.md)]
	
Use Alt + Down Arrow to expand the **TypePropertyEditor**'s drop-down window.

### VisibleInReportsTypePropertyEditor
	
Control: [](xref:DevExpress.XtraEditors.ImageComboBoxEdit) editor from the XtraEditors Library.
	
Repository Item: [](xref:DevExpress.XtraEditors.Repository.RepositoryItemImageComboBox) item from the XtraEditors Library.
	
Description:
	
The editor is inherited from `TypePropertyEditor`. Used by the [Reports V2 Module](xref:113591). It lists the types of business classes that have the `VisibleInReports` property of the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelClass) node set to `true`.

## Customize the Types List

Type Property Editors use the `LocalizedClassInfoTypeConverter` [type converter](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.typeconverter) to create the list of values displayed in the editor's combo box. This converter returns persistent types only. To add all registered [non-persistent](xref:116516) types to this collection, follow these steps:

1. Create a custom converter. Inherit `LocalizedClassInfoTypeConverter` and set the `AllowAddNonPersistentObjects` field value to `true`.

    ```csharp
    using DevExpress.Persistent.Base;
    // ...
    public class MyLocalizedClassInfoTypeConverter : LocalizedClassInfoTypeConverter {
        public MyLocalizedClassInfoTypeConverter() {
            AllowAddNonPersistentObjects = true;
        }
    }
    ```

2. Pass the custom converter to the [TypeConverter](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.typeconverterattribute) attribute.

    ```csharp
    using System.ComponentModel;
    using DevExpress.Xpo;
    using DevExpress.ExpressApp.Utils;
    // ...
    [ValueConverter(typeof(TypeToStringConverter))]
    [TypeConverter(typeof(LocalizedClassInfoTypeConverter))]
    [Size(SizeAttribute.Unlimited)]
    public Type DataType {
        get { return GetPropertyValue<Type>(nameof(DataType)); }
        set { SetPropertyValue<Type>(nameof(DataType), value); }
    }
    ```

3. Override the `AddCustomItems` method in your custom converter to add specific types to the collection.

    ```csharp
    using DevExpress.Persistent.Base;
    // ...
    public class MyLocalizedClassInfoTypeConverter : LocalizedClassInfoTypeConverter {
        // ...
        public override void AddCustomItems(List<Type> list) {
        list.Add(typeof(MyType));
        list.Sort(this);
        base.AddCustomItems(list);
        }
    }
    ```

4. Override the `GetSourceCollection` method to create the entire collection manually.


    ```csharp
    using DevExpress.Persistent.Base;
    // ...
    public class MyLocalizedClassInfoTypeConverter : LocalizedClassInfoTypeConverter {
        // ...
        public override List<Type> GetSourceCollection(ITypeDescriptorContext context) {
            List<Type> result = new List<Type>();
            // Populate the type list here.
            return result;
        }
    }
    ```

> [!TIP]
> You can see more customization techniques in the [How to hide or filter out certain types from the drop-down editor for the System.Type properties](https://supportcenter.devexpress.com/ticket/details/t324232/how-to-hide-or-filter-out-certain-types-from-the-drop-down-editor-for-the-system-type) KB article.
