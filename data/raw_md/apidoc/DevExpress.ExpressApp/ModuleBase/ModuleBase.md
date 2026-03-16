---
uid: DevExpress.ExpressApp.ModuleBase
name: ModuleBase
type: Class
summary: The base class for XAF [modules](xref:118046).
syntax:
  content: 'public class ModuleBase : Component, ISupportSetup'
seealso:
- linkId: DevExpress.ExpressApp.ModuleBase._members
  altText: ModuleBase Members
- linkId: "112569"
---

The presence of a `ModuleBase` class descendant in a standard Class Library project indicates that this is a module project.


You can use modules to customize the [Application Model](xref:112580) when it is being loaded.

### Collect Types Declared Within the Module: Performance Optimization

XAF uses [reflection](https://learn.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/reflection) to collect all types declared in the current module. To optimize type collection in your application, override the following methods:

* `GetDeclaredExportedTypes()`. Collects business classes available in the assembly and exports them to the [Application Model](xref:112580).

* `GetDeclaredControllerTypes()`. Collects Controllers available in the assembly and exports them to the [Application Model](xref:112580).

* `GetRegularTypes()`. Collects built-in types required (business objects, `DbContext` descendants, Controllers, List and Property Editors, and others).

> [!NOTE]
> If you override the `GetRegularTypes` method, XAF stops collecting the types declared in the module and you need to register each new Business Object, Controller, or Editor in this method. However, you do not need to register types that are already returned by overridden `GetDeclaredExportedTypes` and `GetDeclaredControllerTypes` methods.

* `RegisterEditorDescriptors()`. Use it to disable reflection.

### Load Additional Modules
    
Use the `GetRequiredModuleTypesCore` method to add the required modules to the Application Model together with the current module. The current module should have a reference to the modules that you want to add.

### Add Custom Nodes and Properties
    
Override the [ModuleBase.ExtendModelInterfaces](xref:DevExpress.ExpressApp.ModuleBase.ExtendModelInterfaces(DevExpress.ExpressApp.Model.ModelInterfaceExtenders)) method to add required nodes or properties. If you need to add a custom node, first declare its interface by inheriting from [](xref:DevExpress.ExpressApp.Model.IModelNode). For more information, see [Extend and Customize the Application Model in Code](xref:112810).

### Update the Application Model Using the Generator Updaters
    
Override the [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method to add Generator Updaters that update the Application Model.

### Add External Business Objects and Controllers to the Application Model
    
Override the `GetDeclaredControllerTypes` and `GetDeclaredExportedTypes` methods as displayed in the following code snippet:

# [C#](#tab/tabid-csharp)

```csharp
namespace MySolution.Module {  
    public sealed partial class MySolutionModule : ModuleBase {  
        protected override IEnumerable<Type> GetDeclaredControllerTypes() {  
            var originalList = (Type[])base.GetDeclaredControllerTypes();  
            var newList = originalList.ToList();  
            newList.Add(typeof(ClassLibrary1.CustomController));  
            return newList;  
        }  
        protected override IEnumerable<Type> GetDeclaredExportedTypes() {  
            var originalList = base.GetDeclaredExportedTypes();  
            var newList = originalList.ToList();  
            newList.Add(typeof(ClassLibrary1.MyCustomTask));  
            return newList;  
        }  
    }  
}  
```
***

### Update the Database Using Module Updaters
    
Override the [ModuleBase.GetModuleUpdaters](xref:DevExpress.ExpressApp.ModuleBase.GetModuleUpdaters(DevExpress.ExpressApp.IObjectSpace,System.Version)) method to add [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) objects that update the database.

### Customize Type Information
    
Override the [ModuleBase.CustomizeTypesInfo](xref:DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)) method to customize information about a particular class or property before it is loaded to the Application Model. For more information, refer to the following topic: [](xref:113583).

### Register a List or Property Editor
    
Override the protected `RegisterEditorDescriptor` method to disable the reflection mechanism that collects information about types decorated by [](xref:DevExpress.ExpressApp.Editors.ListEditorAttribute) and [](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute). This expedites application startup.

> [!NOTE]
> In this case, Editors that are decorated by [](xref:DevExpress.ExpressApp.Editors.ListEditorAttribute) and [](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute) are not registered.

Use [EditorDescriptorsFactory.RegisterListEditorAlias](xref:DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterListEditorAlias*) and [EditorDescriptorsFactory.RegisterListEditor](xref:DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterListEditor*) methods to register your List Editor with its alias.

To register a Property Editor, use [EditorDescriptorsFactory.RegisterPropertyEditorAlias](xref:DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterPropertyEditorAlias*) and [EditorDescriptorsFactory.RegisterPropertyEditor](xref:DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterPropertyEditor*) methods.

You can associate an [](xref:DevExpress.ExpressApp.Editors.EditorAliases) enumerator value or a custom alias with a target type. You can register one alias for WinForms and ASP.NET Core Blazor Editors in the base module project and locate corresponding Editors in platform-dependent projects. If you use platform-agnostic Editors for certain types, specify a string alias to use them in a platform-independent module.

> [!NOTE]
> The Editor registered for the `Object` type serves as a fallback/default editor for objects and properties not associated with a specific Editor type.

The following example registers a default List Editor:

# [C#](#tab/tabid-csharp)

```csharp
public class MyModule : ModuleBase {
    //...
    protected override void RegisterEditorDescriptors(EditorDescriptorsFactory 
    editorDescriptorsFactory) {
        editorDescriptorsFactory.RegisterListEditorAlias("CustomListEditorAlias",
        typeof(object), true);
        editorDescriptorsFactory.RegisterListEditor("CustomListEditorAlias", 
        typeof(object), typeof(GridListEditor), true);
    }
}
```
***

The list below describes how to customize this example.

* Pass type `Object` as the `elementType` parameter and `false` as the `isDefaultEditor` parameter. The method add the Editor to the [IModelViews.DefaultListEditor](xref:DevExpress.ExpressApp.Model.IModelViews.DefaultListEditor) list. This enables this Editor in the Model Editor.
* To register the default List Editor for objects of a specific type, pass the target type to the methods' `elementType` parameter and set the `isDefaultEditor` parameter to `true` to mark this Editor as the default editor for this type.
* Pass a type as the `elementType` parameter and `false` as the `isDefaultEditor` parameter. The method adds the List Editor to the [IModelClass.EditorType](xref:DevExpress.ExpressApp.Model.IModelClass.EditorType) list for the specified type. This allows you to choose this Editor in the Model Editor.
* Use the `classHandler` parameter of the `RegisterListEditorAlias` method if you want to register a number of Editors for one type and choose an editor according to custom logic. The editor that matches the specified conditions is applied to the current type first.
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    public class MyModule : ModuleBase {
        //...
        protected override void RegisterEditorDescriptors(EditorDescriptorsFactory editorDescriptorsFactory) {
            //...
            editorDescriptorsFactory.RegisterListEditorAlias("MyAlias", typeof(object), IsCriteriaProperty); 
        }
        private static bool IsCriteriaProperty(IModelClass modelClass) {
            //...    
        }
    }
    ```
    ***

The following example registers a default Property Editor:

# [C#](#tab/tabid-csharp)

```csharp
public class MyModule : ModuleBase {
    //...
    protected override void RegisterEditorDescriptors(EditorDescriptorsFactory 
    editorDescriptorsFactory) {
        //...
        editorDescriptorsFactory.RegisterPropertyEditorAlias("CustomPropertyEditorAlias",
        typeof(object), true);
        editorDescriptorsFactory.RegisterPropertyEditor("CustomPropertyEditorAlias", 
        typeof(object), typeof(DefaultPropertyEditor), true);
    }
}
```
***

> [!NOTE]
> To set a Property Editor as default for properties with protected content, implement the `IProtectedContentEditor` interface in the Property Editor.

The list below describes how you can modify this example.

* Pass type `Object` as the `elementType` parameter and `false` as the `isDefaultEditor` parameter. The method adds the Editor to the [IModelRegisteredViewItem.DefaultItemType](xref:DevExpress.ExpressApp.Editors.IModelRegisteredViewItem.DefaultItemType) list of default Property Editors or the [IModelRegisteredPropertyEditors.ProtectedContentPropertyEditor](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditors.ProtectedContentPropertyEditor) list if your Editor is for the properties with protected content. This allows you to choose this Editor in the Model Editor.
* To register the default Property Editor for the properties of a specific type, pass the target type to the methods' `elementType` parameter and set the `isDefaultEditor` parameter to `false` to mark this Editor as the default editor for this type.
* Specify the target type in the methods' `elementType` parameter and set the `isDefaultEditor` parameter to `false` to add the Property Editor to the [IModelRegisteredPropertyEditor.EditorType](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.EditorType) list of Property Editors for the specified type. Then, you can choose this Editor in the Model Editor.
* Use the `memberHandler` parameter of the `RegisterPropertyEditorAlias` method if you want to register a number of Editors for properties of one type and choose the appropriate Editor according to the logic implemented in it. In different situations, the Editor satisfying the conditions is applied to current type first. Editors registered with this parameter have priority over Editors registered without it. For the Editor registered with the `memberHandler` parameter, the new node is created in the Model Editor's **View Items** | **PropertyEditors** node.
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    public class MyModule : ModuleBase {
        //...
        protected override void RegisterEditorDescriptors(EditorDescriptorsFactory 
        editorDescriptorsFactory) {
            //... 
            editorDescriptorsFactory.RegisterPropertyEditorAlias("MyAlias", 
            typeof(DateTime), IsMemberCompatibleHandler);
        }
        private static bool IsMemberCompatibleHandler(IModelMember modelMember) {
            //...
        }
    }
    ```
    ***

You do not have to create instances of `ModuleBase` class descendants. They are created automatically.

### Add External Business Objects and Controllers to the Application Model

XAF uses [reflection](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection) to collect classes and Controllers from each [module](xref:118046) and build an [Application Model](xref:112579). Use the following techniques to customize this process: 

* Use the [ModuleBase.AdditionalControllerTypes](xref:DevExpress.ExpressApp.ModuleBase.AdditionalControllerTypes) and [ModuleBase.AdditionalExportedTypes](xref:DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes) properties to specify business classes and [Controllers](xref:112621) that should be loaded to the Application Model:

    **File:** _MySolution.Module/Module.cs_
    # [C#](#tab/tabid-csharp)
    
    ```csharp{5,6}
    namespace MySolution.Module {
        public sealed partial class MySolutionModule : ModuleBase {
            public MySolutionModule() {
                InitializeComponent();
                AdditionalControllerTypes.Add(typeof(ClassLibrary1.Controller1));
                AdditionalExportedTypes.Add(typeof(ClassLibrary1.PersistentClass1));
            }
        // ...
        }
    }
    ```
    ***

* Override the `GetDeclaredControllerTypes` and `GetDeclaredExportedTypes` methods of the [ModuleBase](xref:DevExpress.ExpressApp.ModuleBase) class to add external business objects and Controllers to the Application Model:
    
    **File:** _MySolution.Module/Module.cs_
    # [C#](#tab/tabid-csharp)
    ```csharp
    namespace MySolution.Module {  
        public sealed partial class MySolutionModule : ModuleBase {  
            protected override IEnumerable<Type> GetDeclaredControllerTypes() {  
                var originalList = (Type[])base.GetDeclaredControllerTypes();  
                var newList = originalList.ToList();  
                newList.Add(typeof(ClassLibrary1.CustomController));  
                return newList;  
            }  
            protected override IEnumerable<Type> GetDeclaredExportedTypes() {  
                var originalList = base.GetDeclaredExportedTypes();  
                var newList = originalList.ToList();  
                newList.Add(typeof(ClassLibrary1.MyCustomTask));  
                return newList;  
            }  
        }  
    }  
    ```
    ***

### Replace Data Model Classes in a Built-In Module

If you want to use a custom entity type in a built-in module, configure this type in the Application Builder's module settings. For more information on how to do this, refer to the following topic: <xref:118046>.
