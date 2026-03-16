---
uid: "405312"
title: Display a Tree List With Flat Data Objects (ASP.NET Core Blazor)
owner: Anastasiya Kisialeva
---
# Display a Tree List With Flat Data Objects (ASP.NET Core Blazor)

ASP.NET Core Blazor @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor component can display a [flat data](xref:112836#flat-data-structure) object collection as a tree-like structure. To make this possible, objects in the data source should have relationships defined by Key and Parent Key properties. This topic shows an example of such implementation.

> [!NOTE]
> In this scenario, classes do not need to implement the `ITreeNode` interface.

## Initial Data Model Implementation

First, implement a simple class with a `ParentObjectId` property that targets a parent node's key value.

`HasChildren` property allows you to use [Queryable](xref:402925) data access mode. In this mode, Tree List loads child nodes from the database only when you expand the parent node. The `HasChildren` property shows whether the parent object should contain children.

> [!NOTE]
> * If you make this property persistent, XAF initially queries only visible nodes from the database.
> * If this property is calculated, XAF loads the next level to allow the Tree List to evaluate whether nodes have children.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.ObjectModel;

namespace SolutionName.Module.BusinessObjects;
[DefaultClassOptions]
public class Category : BaseObject {
   public virtual string Name { get; set; }
   [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
   public virtual Guid ParentObjectId { get; set; }

   // Add this property if you use Queryable data access mode.
   [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
   [PersistentAlias("[<MyApplication.Module.BusinessObjects.Category>][ParentObjectId = ^.ID and ID != ^.ID]")]
   public bool HasChildren => EvaluateAlias<bool>();
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;

namespace SolutionName.Module.BusinessObjects;
[DefaultClassOptions]
public class Category : BaseObject {
    public Category(Session session) : base(session) { }

    private string name;
    public string Name {
        get => name;
        set => SetPropertyValue(nameof(Name), ref name, value);
    }

    private Guid parentObjectId;
    [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
    public Guid ParentObjectId {
        get => parentObjectId;
        set => SetPropertyValue(nameof(ParentObjectId), ref parentObjectId, value);
    }

    // Add this property if you use Queryable data access mode.
    [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
    [PersistentAlias("[<SolutionName.Module.BusinessObjects.Category>][ParentObjectId = ^.Oid and Oid != ^.Oid]")]
    public bool HasChildren => Convert.ToBoolean(EvaluateAlias("HasChildren"));
}
```
***

You can make the `HasChildren` property persistent (stored in the database):

- Add a getter and setter
- Remove the [`PersistentAlias`](xref:DevExpress.ExpressApp.DC.PersistentAliasAttribute) attribute

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
//...
[HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
public virtual bool HasChildren { get; set; }
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
//...
private bool hasChildren;
[HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
public bool HasChildren {
    get {
        return hasChildren;
    }
    set {
        SetPropertyValue(nameof(HasChildren), ref hasChildren, value);
    }
}
```
***

If your application uses EF Core Framework, register the `Category` class in the `DBContext`.

**File:** _SolutionName.Module\BusinessObjects\SolutionNameDbContext.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.EFCore.Updating;
using DevExpress.Persistent.BaseImpl.EF;
using Microsoft.EntityFrameworkCore;

namespace SolutionName.Module.BusinessObjects;
// ...
public class SolutionNameDbContext : DbContext {
    // ...
    public SolutionNameDbContext(DbContextOptions<SolutionNameDbContext> options)
        : base(options) {
    }
    // ...
    public DbSet<Category> Categories { get; set; }

}
```
***

## Step-by-Step Scenario

1. In your ASP.NET Core Blazor project (_SolutionName.Blazor.Server_), open [Model Editor](xref:112582) and navigate to the **Category_ListView** node.
2. In the `EditorType` property, specify the [DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor](xref:DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor) value.
3. Specify the `KeyFieldName`, `ParentKeyFieldName`, and `HasChildrenFieldName` properties as follows:

   | Property | EF Core | XPO |
   |------------|----------------------------------|-------------------------|
   | `HasChildrenFieldName` | `HasChildren` | `HasChildren` |
   | `KeyFieldName` | `ID` | `Oid` |
   | `ParentKeyFieldName` | `ParentObjectId` | `ParentObjectId` |
4. Run the ASP.NET Core Blazor application and click the `Category` item in the navigation control.
5. To create a top-level `Category` object, use the **New** Action.
6. To create a child object, select the parent object in the tree list and click the **New** action.

   XAF displays these objects as a tree in the Category List View:

   ![|XAF Tree List View with Flat Data Objects, DevExpress](~/images/xaf-blazor-list-view-flat-data-objects-treelist-devexpress.png)

## Set Up One-To-Many Relationship (EF Core)

1. Add the `ParentObject` and `Children` properties to the `Category` class. Make `ParentObjectId` nullable to use it as a foreign key.

    **File:** _SolutionName.Module\BusinessObjects\Category.cs_

    # [C#](#tab/tabid-csharp)
    ```csharp{11-12,15}
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    using System.Collections.ObjectModel;

    namespace SolutionName.Module.BusinessObjects;

    [DefaultClassOptions]
    public class Category : BaseObject {
        public virtual string Name { get; set; }
        [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
        public virtual Guid? ParentObjectId { get; set; }
        public virtual Category ParentObject { get; set; }
        [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
        public virtual bool HasChildren { get; set; }
        public virtual IList<Category> Children { get; set; } = new ObservableCollection<Category>();
    }
    ```
    ***

2. To configure the One-to-Many relationship between objects of the `Category` type, use the `OnModelCreating` method of your `DbContext` descendant. 

    **File:** _SolutionName.Module\BusinessObjects\SolutionNameDbContext.cs_

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.Design;
    using DevExpress.ExpressApp.EFCore.DesignTime;
    using DevExpress.ExpressApp.EFCore.Updating;
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.BaseImpl.EF;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
    using Microsoft.EntityFrameworkCore;

    namespace SolutionName.Module.BusinessObjects;
    // ...
    public class SolutionNameDbContext : DbContext {
        // ...
        public SolutionNameDbContext(DbContextOptions<SolutionNameDbContext> options)
            : base(options) {
        }
        protected override void OnModelCreating(ModelBuilder modelBuilder) {
        //...
            var entity = modelBuilder.Entity<Category>();
            entity
                .HasMany(x => x.Children)
                .WithOne(x => x.ParentObject)
                .HasForeignKey(x => x.ParentObjectId);
        //...
        }
    }
    ```
    ***
3. In your ASP.NET Core Blazor project (_SolutionName.Blazor.Server_), open [Model Editor](xref:112582) and navigate to the **Category_Children_ListView** node.
4. In the `EditorType` property, specify the [DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor](xref:DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor) value.
5. Specify the `KeyFieldName`, `ParentKeyFieldName`, and `HasChildrenFieldName` properties as follows:

   | Property | Value |
   |------------|----------------------------------|
   | `HasChildrenFieldName` | `HasChildren` |
   | `KeyFieldName` | `ID` |
   | `ParentKeyFieldName` | `ParentObjectId` |

   These settings also allow your Tree List editor to handle `HasChildren` collection updates automatically.

## Set Up One-To-Many Relationship (XPO)

1. Add the `ParentObject` and `Children` properties to the `Category` class.
2. To configure the One-to-Many relationship between objects of the `Category` type, use the [`Association`](xref:DevExpress.Xpo.AssociationAttribute) attribute.
3. Handle the `CollectionChanged` event of the `Children` collection to update the `HasChildren` property when child objects are removed.

    # [C#](#tab/tabid-csharp)
    ```csharp{19-30,37-38,42}
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl;
    using DevExpress.Xpo;

    namespace SolutionName.Module.BusinessObjects;
    [DefaultClassOptions]
    public class Category : BaseObject {
        public Category(Session session) : base(session) { }

        private string name;
        public string Name {
            get => name;
            set => SetPropertyValue(nameof(Name), ref name, value);
        }
        [PersistentAlias("IsNull(ParentObject.Oid, {00000000-0000-0000-0000-000000000000})")]
        [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
        public Guid ParentObjectId => (Guid)EvaluateAlias();

        private Category parentObject;
        [Association("Parent-Children")]
        public Category ParentObject {
            get => parentObject;
            set {
                var oldParent = parentObject;
                SetPropertyValue(nameof(ParentObject), ref parentObject, value);
                if(value == null && oldParent != null) {
                    oldParent.UpdateHasChildren();
                }
            }
        }
        [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
        public bool HasChildren {
            get => GetPropertyValue<bool>();
            set => SetPropertyValue(nameof(HasChildren), value);
        }

        [Association("Parent-Children")]
        public XPCollection<Category> Children => GetCollection<Category>();

        protected override void OnLoaded() {
            base.OnLoaded();
            Children.CollectionChanged += Children_CollectionChanged;
        }

        private void Children_CollectionChanged(object sender, XPCollectionChangedEventArgs e) {
            if(e.CollectionChangedType == XPCollectionChangedType.AfterRemove) {
                UpdateHasChildren();
            }
        }

        private void UpdateHasChildren()
        {
            HasChildren = Children.Any(x => !x.IsDeleted && x.ParentObject?.Oid == Oid);
        }
        //...
    }
    ```
    ***

4. Create a controller to handle the assignment of the `ParentObject` property when new child objects are created or existing child objects are orphaned.

    **File:** _SolutionName.Blazor.Server\Controllers\CategoryController.cs_

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.Editors;
    using DevExpress.ExpressApp.Blazor.SystemModule;

    namespace SolutionName.Blazor.Server.Controllers;

    public class CategoryController : ObjectViewController<ListView, Category> {
        private TreeNewFlatObjectController newTreeNodeController;
        private TreeFlatParentObjectUpdateController parentUpdateController;

        protected override void OnActivated() {
            base.OnActivated();
            if(View.Editor is not DxTreeListEditor) {
                return;
            }

            newTreeNodeController = Frame.GetController<TreeNewFlatObjectController>();
            newTreeNodeController.ProcessNewTreeObject += NewTreeNodeController_ProcessNewTreeObject;

            parentUpdateController = Frame.GetController<TreeFlatParentObjectUpdateController>();
            parentUpdateController.ChildNodeOrphaned += ParentUpdateController_ChildNodeOrphaned;
        }

        protected override void OnDeactivated() {
            base.OnDeactivated();
            if(View.Editor is not DxTreeListEditor) {
                return;
            }

            if(newTreeNodeController != null) {
                newTreeNodeController.ProcessNewTreeObject -= NewTreeNodeController_ProcessNewTreeObject;
                newTreeNodeController = null;
            }

            if(parentUpdateController != null) {
                parentUpdateController.ChildNodeOrphaned -= ParentUpdateController_ChildNodeOrphaned;
                parentUpdateController = null;
            }
        }

        private void NewTreeNodeController_ProcessNewTreeObject(object sender, ProcessNewTreeObjectEventArgs e) {
            var node = (Category)e.NewTreeNode;
            var parent = (Category)e.ParentNode;
            node.ParentObject = parent;
        }

        private void ParentUpdateController_ChildNodeOrphaned(object sender, ChildNodeOrphanedEventArgs e) {
            var node = (Category)e.Node;
            node.ParentObject = null;
        }
    }
    ```
    ***

5. In your ASP.NET Core Blazor project (_SolutionName.Blazor.Server_), open [Model Editor](xref:112582) and navigate to the **Category_Children_ListView** node.
6. In the `EditorType` property, specify the [DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor](xref:DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor) value.
7. Specify the `KeyFieldName`, `ParentKeyFieldName`, and `HasChildrenFieldName` properties as follows:

   | Property | Value |
   |------------|----------------------------------|
   | `HasChildrenFieldName` | `HasChildren` |
   | `KeyFieldName` | `Oid` |
   | `ParentKeyFieldName` | `ParentObjectId` |

