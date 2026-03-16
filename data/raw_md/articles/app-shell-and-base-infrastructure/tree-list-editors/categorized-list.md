---
uid: "112838"
seealso: []
title: Categorized List (Windows Forms)
owner: Ekaterina Kiseleva
---
# Categorized List (Windows Forms)

When data is displayed as a tree, you may need to show the objects associated with the currently selected node in the same List View. **XAF** enables you to do this by implementing the [](xref:DevExpress.Persistent.Base.General.ICategorizedItem) interface in the associated objects, and using the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.CategorizedListEditor) provided by the TreeList Editors module. This topic demonstrates an implementation of categorized list with the business classes defined in the [Display a Tree List using the ITreeNode Interface](xref:112837) topic.

> [!Tip]
> [!include[CodeCentralObjectE1125](~/templates/CodeCentralExampleNote.md)] [https://supportcenter.devexpress.com/ticket/details/e1125/xaf-how-to-use-tree-list-editors-to-display-list-views-for-asp-net-core-blazor-and](https://supportcenter.devexpress.com/ticket/details/e1125/xaf-how-to-use-tree-list-editors-to-display-list-views-for-asp-net-core-blazor-and).

In the [Display a Tree List using the ITreeNode Interface](xref:112837) topic, the ProjectGroup, Project and ProjectArea classes are implemented by inheriting from an abstract Category class, which implements the [](xref:DevExpress.Persistent.Base.General.ITreeNode) interface. Now, we will implement the Issue class that will be related to the Category class by the Many-to-One relationship. In addition, to display the Issue List View via the **CategorizedListEditor**, the Issue class will implement the **ICategorizedItem** interface. For details on this interface and the CategorizedListEditor, refer to the [TreeList Editors Module Overview](xref:112836) topic.

Implement the Issue class as shown in the code below:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base.General;
using System.ComponentModel.DataAnnotations;
//...
[DefaultClassOptions]
public class Issue : BaseObject, ICategorizedItem {
   public virtual Category Category { get; set; }
   public virtual string Subject { get; set; }
   public virtual string Description { get; set; }

   ITreeNode ICategorizedItem.Category {
      get {
          return Category;
      }
      set {
         Category = (Category)value;
      }
   }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base.General;
//...
[DefaultClassOptions]
public class Issue : BaseObject, ICategorizedItem {
   private Category category;
   private string subject;
   private string description;
   public Issue(Session session) : base(session) {}
   public Issue(Session session, string subject) : base(session) {
      this.subject = subject;
   }
   [Association("Category-Issues")]
   public Category Category {
      get {
         return category;
      }
      set {
         SetPropertyValue(nameof(Category), ref category, value);
      }
   }
   public string Subject {
      get {
         return subject;
      }
      set {
         SetPropertyValue(nameof(Subject), ref subject, value);
      }
   }
   public string Description {
      get {
         return description;
      }
      set {
         SetPropertyValue(nameof(Description), ref description, value);
      }
   }
   ITreeNode ICategorizedItem.Category {
      get {
          return Category;
      }
      set {
         Category = (Category)value;
      }
   }
}
```
***

> [!NOTE]
> The public property that is returned by the private **Category** property, which implicitly implements the **ICategorizedItem** interface, must be called "Category". This is currently required by the internal infrastructure.

Modify the Category class to add an association with Issue objects:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[NavigationItem]
public abstract class Category : BaseObject, ITreeNode {
    public virtual IList<Issue> Issues { get; set; } = new ObservableCollection<Issue>();
    private List<Issue> allIssues;

    [NotMapped]
    public IList<Issue> AllIssues {
        get {
            if(allIssues == null) {
                allIssues = new List<Issue>();
                CollectIssuesRecursive(this, allIssues);
            }
            return allIssues;
        }
    }

    private void CollectIssuesRecursive(Category issueCategory, List<Issue> target) {
        target.AddRange(issueCategory.Issues);
        foreach(Category childCategory in issueCategory.Children) {
            CollectIssuesRecursive(childCategory, target);
        }
    }
   //...
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[NavigationItem]
public abstract class Category : BaseObject, ITreeNode {
   [Association("Category-Issues")]
   public XPCollection<Issue> Issues {
      get {
         return GetCollection<Issue>(nameof(Issues));
      }
   }
   private XPCollection<Issue> allIssues;
   public XPCollection<Issue> AllIssues {
      get {
         if (allIssues == null) {
            allIssues = new XPCollection<Issue>(Session, false);
            CollectIssuesRecursive(this, allIssues);
            allIssues.BindingBehavior = CollectionBindingBehavior.AllowNone;
         }
         return allIssues; 
      }
   }   
   private void CollectIssuesRecursive(Category issueCategory, XPCollection<Issue> target) {
      target.AddRange(issueCategory.Issues);
      foreach (Category childCategory in issueCategory.Children) {
         CollectIssuesRecursive(childCategory, target);
      }
   }
  //...
}
```
***

Check that the TreeList Editors module is added to the Windows Forms application project, and run the application. Invoke the Issue List View. Select a tree node in the tree list to the left and execute the New Action, to create an Issue for the corresponding Category object. To the right of the tree list, a list of Issue objects associated with the currently selected tree node is displayed.

![CategorizedListEditor](~/images/categorizedlisteditor115620.png)
