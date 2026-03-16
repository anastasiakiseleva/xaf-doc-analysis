---
uid: "112839"
seealso:
- linkId: "404214"
title: Display a Tree List using the HCategory Class
owner: Ekaterina Kiseleva
---
# Display a Tree List using the HCategory Class

[!include[tree-list-how-to-intro](~/templates/tree-list-how-to-intro.md)]

This topic demonstrates the `HCategory` class that implements the `ITreeNode` interface out of the box. XAF supplies this class with the [Business Class Library](xref:112571), and you can use it instead of implementing the `ITreeNode` class from scratch.

> [!Tip]
> [!include[CodeCentralObjectE1125](~/templates/CodeCentralExampleNote.md)] [https://supportcenter.devexpress.com/ticket/details/e1125/xaf-how-to-use-tree-list-editors-to-display-list-views-for-asp-net-core-blazor-and](https://supportcenter.devexpress.com/ticket/details/e1125/xaf-how-to-use-tree-list-editors-to-display-list-views-for-asp-net-core-blazor-and).

The `HCategory` class is implemented in such a way that its `Parent` and `Children` properties can reference objects of the `HCategory` type only.

## Add HCategory Class to Your Business Model

In the **Solution Explorer**, go to the **YourSolutionName.Module** project and open the _Module.cs_ file. Add the `HCategory` class to the `AdditionalExportedTypes` collection.

For more information on how to add a business class to your project, refer to the following topic: [](xref:112847)

# [C# (EF Core)](#tab/tabid-efcore)

```csharp
//...
namespace MySolution.Module;
//...
public sealed class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        //...
        AdditionalExportedTypes.Add(typeof(DevExpress.Persistent.BaseImpl.EF.HCategory));
    }
//...
}
```

# [XPO](#tab/tabid-xpo)

```csharp
//...
namespace MySolution.Module;
//...
public sealed class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        //...
        AdditionalExportedTypes.Add(typeof(DevExpress.Persistent.BaseImpl.HCategory));
    }
//...
}
```

***

> [!TIP]
> If your application uses Entity Framework Core, register the `HCategory` class in your application's DBContext:
> ```csharp
> using MySolution.Module.BusinessObjects;
> 
> namespace  MySolution.Module.BusinessObjects {
>     public class MySolutionEFCoreDbContext : DbContext {
>         //...
>         public DbSet<HCategory> HCategories { get; set; }
>     }
> }
> ```

## Add HCategory to the Navigation Control

To add the `HCategory` class to the navigation control, open the Model Editor for the current module and add the **HCategory** node to the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node. For more information, refer to the following topic: [Add an Item to the Navigation Control](xref:402131).

## Enable the TreeList Editors Module in Your Application

To display the `HCategory` object as a tree, add the TreeList Editors module to the application. For more information, refer to the following section: [Add the TreeList Editors Module to Your Application](xref:112836#add-the-treelist-editors-module-to-your-application).

## Run the Application

Run the application. Click the `HCategory` item in the navigation control. Use the **New** Action to create `HCategory` objects. XAF displays these objects as a tree in the `HCategory` List View:

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor HCategory, DevExpress](~/images/xaf-blazor-treelist-hcategory-devexpress.png)
Windows Forms
:   ![XAF Windows Forms HCategory, DevExpress](~/images/hcategory115623.png)

## Additional Information (Windows Forms)

You can also display a collection of items for each `HCategory` node to the right of the tree list. For more information, refer to the following topic: [](xref:112838).

To extend the `HCategory` class, inherit from it.

To implement the `ITreeNode` interface from scratch, refer to the following topic: [](xref:112837).

To see the `HCategory` class implementation, refer to the following folders where you can find the _HCategory.cs_ file:
* _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]Xpo_
* _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]EFCore_

> [!NOTE]
> The `TreeListEditor` and `CategorizedListEditor` cannot properly display a tree if the List View's object type derives from the base type that implements the `ITreeNode` interface and the hierarchy contains base type objects.
> 
> Example: A tree contains `HCategoryDerived` descendant objects that have child `HCategory` objects. When a user invokes a List View for the descendant type (`HCategoryDerived`), neither `TreeListEditor` nor `CategorizedListEditor` can correctly display this structure. To correctly display such a tree, you need to invoke a List View for the base type (`HCategory` in this case).
