---
uid: "112837"
title: Display a Tree List using the ITreeNode Interface
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-use-tree-list-editors-to-display-list-views
  altText: 'GitHub Example: XAF - How to Use Tree List Editors to Display List Views For ASP.NET Core Blazor And Windows Forms'
---
# Display a Tree List using the ITreeNode Interface

[!include[tree-list-how-to-intro](~/templates/tree-list-how-to-intro.md)]

This topic demonstrates the implementation of the `ITreeNode` interface.

> [!Tip]
> [!include[CodeCentralObjectE1125](~/templates/CodeCentralExampleNote.md)] [https://supportcenter.devexpress.com/ticket/details/e1125/xaf-how-to-use-tree-list-editors-to-display-list-views-for-asp-net-core-blazor-and](https://supportcenter.devexpress.com/ticket/details/e1125/xaf-how-to-use-tree-list-editors-to-display-list-views-for-asp-net-core-blazor-and).
> 
> [!include[template-how-to-implement-tree-list-editor-example](~/templates/template-how-to-implement-tree-list-editor-example.md)]

Follow instructions in this example to implement the following tree structure:

![CategoryTreeList](~/images/categorytreelist115622.png)

![CategoryTreeList Legend](~/images/categorytreelist-legend115624.png)

You need the following classes:
* ProjectGroup
* Project
* ProjectArea

Derive these classes from an abstract class that implements the `ITreeNode` interface. To display a tree of these objects, add an item that corresponds to that abstract class to the navigation control. When you click this item, XAF organizes all objects of the types derived from the abstract class in a tree via the Tree List editors (you need to add the TreeList Editors module to the application).


> [!NOTE]
> Business classes you implement in this example must meet the following requirements:
> 
> * The parent and child classes corresponding to tree list nodes should be derived from the same persistent class that implements the `ITreeNode` interface. In this example, the `ProjectGroup`, `Project`, and `ProjectArea` classes are derived from the `Category` class.
> * It is impossible to have more than one root class in a Tree List. In this example, the `ProjectGroup` is the root class.

1. Implement an abstract `Category` class as the following code snippet demonstrates:
	
	# [C# (EF Core)](#tab/tabid-csharp-ef)
	
	```csharp
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.Base.General;
	using System.ComponentModel;
	using DevExpress.Persistent.BaseImpl.EF;

	namespace MySolution.Module.BusinessObjects;
	[NavigationItem]
	public abstract class Category : BaseObject, ITreeNode {
		protected abstract ITreeNode GetParent();
		protected abstract IBindingList GetChildren();

		public virtual string Name { get; set; }
		#region ITreeNode
		IBindingList ITreeNode.Children {
			get {
				return GetChildren();
			}
		}
		string ITreeNode.Name {
			get {
				return Name;
			}
		}
		ITreeNode ITreeNode.Parent {
			get {
				return GetParent();
			}
		}
		#endregion
	}
	// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
	```

	# [C# (XPO)](#tab/tabid-csharp-xpo)
	```csharp
	using DevExpress.Xpo;
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.BaseImpl;
	using DevExpress.Persistent.Base.General;
	using System.ComponentModel;

	namespace MySolution.Module.BusinessObjects;
	[NavigationItem]
	public abstract class Category : BaseObject, ITreeNode {
		private string name;
		protected abstract ITreeNode GetParent();
		protected abstract IBindingList GetChildren();
		public Category(Session session) : base(session) { }
		public string Name {
			get {
				return name;
			}
			set {
				SetPropertyValue("Name", ref name, value);
			}
		}
		#region ITreeNode
		IBindingList ITreeNode.Children {
			get {
				return GetChildren();
			}
		}
		string ITreeNode.Name {
			get {
				return Name;
			}
		}
		ITreeNode ITreeNode.Parent {
			get {
				return GetParent();
			}
		}
		#endregion
	}
	```
	***
	
	Apply the [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) to add the corresponding navigation item to the navigation control. This overrides the `Parent` and `Children` properties in the descendant classes to return objects of the required types.
	

2. Implement the `ProjectGroup`, `Project`, and `ProjectArea` classes. Derive these classes from the `Category` class.
	
	**Entity Framework Core classes:**

	# [ProjectGroup.cs](#tab/tabid-csharp-projectgroup)

	```csharp
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.Base.General;
	using System.Collections.ObjectModel;
	using System.ComponentModel;

	namespace MySolution.Module.BusinessObjects;
	[DefaultClassOptions]
	public class ProjectGroup : Category {
		public ProjectGroup() {
			projects.CollectionChanged += (s, e) => children?.ResetBindings();
		}
		ObservableCollection<Project> projects = new ObservableCollection<Project>();
		protected override ITreeNode GetParent() {
			return null;
		}
		protected override IBindingList GetChildren() {
			if (children == null) {
				children = new BindingList<Project>(Projects);
			}
			return children;
		}
		BindingList<Project> children;
		[DevExpress.ExpressApp.DC.Aggregated]
		public virtual ObservableCollection<Project> Projects { get => projects; }
	}
	// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
	```

	# [Project.cs](#tab/tabid-csharp-project)

	```csharp
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.Base.General;
	using System.Collections.ObjectModel;
	using System.ComponentModel;

	namespace MySolution.Module.BusinessObjects;
	[DefaultClassOptions]
	public class Project : Category {
		public Project() {
			projectAreas.CollectionChanged += (s, e) => children?.ResetBindings();
		}
		protected override ITreeNode GetParent() {
			return ProjectGroup;
		}
		protected override IBindingList GetChildren() {
			if (children == null) {
				children = new BindingList<ProjectArea>(ProjectAreas);
			}
			return children;
		}
		[DevExpress.ExpressApp.DC.Aggregated]
		public virtual ObservableCollection<ProjectArea> ProjectAreas { get => projectAreas; }
		ObservableCollection<ProjectArea> projectAreas = new ObservableCollection<ProjectArea>();
		BindingList<ProjectArea> children;
		public virtual ProjectGroup ProjectGroup { get; set; }
	}

	// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
	```

	# [ProjectArea.cs](#tab/tabid-csharp-projectarea)

	```csharp
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.Base.General;
	using System.ComponentModel;

	namespace MySolution.Module.BusinessObjects;
	[DefaultClassOptions]
	public class ProjectArea : Category {
		protected override ITreeNode GetParent() {
			return Project;
		}
		BindingList<object> emptyChildren = new BindingList<object>();
		protected override IBindingList GetChildren() {
			return emptyChildren;
		}
		public virtual Project Project { get; set; }
	}

	// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
	```
	***

	**XPO classes:**

	# [ProjectGroup.cs](#tab/tabid-csharp-projectgroup)
	
	```csharp
	using DevExpress.Xpo;
	using DevExpress.Persistent.Base.General;
	using System.ComponentModel;

	namespace MySolution.Module.BusinessObjects;
	public class ProjectGroup : Category {
		protected override ITreeNode GetParent() {
			return null;
		}
		protected override IBindingList GetChildren() {
			return Projects;
		}
		public ProjectGroup(Session session) : base(session) { }
		public ProjectGroup(Session session, string name)
			: base(session) {
			this.Name = name;
		}
		[Association("ProjectGroup-Projects"), Aggregated]
		public XPCollection<Project> Projects {
			get {
				return GetCollection<Project>("Projects");
			}
		}
	}
	```

	# [Project.cs](#tab/tabid-csharp-project)
	
	```csharp
	using DevExpress.Xpo;
	using DevExpress.Persistent.Base.General;
	using System.ComponentModel;

	namespace MySolution.Module.BusinessObjects;
	public class Project : Category {
		private ProjectGroup projectGroup;
		protected override ITreeNode GetParent() {
			return projectGroup;
		}
		protected override IBindingList GetChildren() {
			return ProjectAreas;
		}
		public Project(Session session) : base(session) { }
		public Project(Session session, string name)
			: base(session) {
			this.Name = name;
		}
		[Association("ProjectGroup-Projects")]
		public ProjectGroup ProjectGroup {
			get {
				return projectGroup;
			}
			set {
				SetPropertyValue("ProjectGroup", ref projectGroup, value);
			}
		}
		[Association("Project-ProjectAreas"), Aggregated]
		public XPCollection<ProjectArea> ProjectAreas {
			get {
				return GetCollection<ProjectArea>("ProjectAreas");
			}
		}
	}
	```

	# [ProjectArea.cs](#tab/tabid-csharp-projectarea)
	
	```csharp
	using DevExpress.Xpo;
	using DevExpress.Persistent.Base.General;
	using System.ComponentModel;

	namespace MySolution.Module.BusinessObjects;
	public class ProjectArea : Category {
		private Project project;
		protected override ITreeNode GetParent() {
			return project;
		}
		protected override IBindingList GetChildren() {
			return new BindingList<object>();
		}
		public ProjectArea(Session session) : base(session) { }
		public ProjectArea(Session session, string name)
			: base(session) {
			this.Name = name;
		}
		[Association("Project-ProjectAreas")]
		public Project Project {
			get {
				return project;
			}
			set {
				SetPropertyValue("Project", ref project, value);
			}
		}
	}
	```
	***
	
	> [!TIP]
    > If your application uses Entity Framework Core, register new classes in your application's DBContext:
	> ```csharp
	> using MySolution.Module.BusinessObjects;
	> 
	> namespace  MySolution.Module.BusinessObjects;
	> public class MySolutionEFCoreDbContext : DbContext {
	>     //...
	>     public DbSet<Category> Categories { get; set; }
	>     public DbSet<Project> Projects { get; set; }
	>     public DbSet<ProjectArea> ProjectAreas { get; set; }
	>     public DbSet<ProjectGroup> ProjectGroups { get; set; }
	> }
	> ```

3. In a Windows Forms project, add the TreeList Editors module as described in the following topic: [](xref:112836).
4. Run the application. Click the `Category` item in the navigation control and use the **New** Action to create `ProjectGroup`, `Project`, and `ProjectArea` objects. The `Category` List View displays these objects as a hierarchical tree:

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor Tree List for ITreeNode, DevExpress](~/images/xaf-blazor-treelist-itreenode-devexpress.png)
Windows Forms
:   ![XAF Windows Forms Tree List for ITreeNode, DevExpress](~/images/treeListeditorITreeNode.png)

> [!NOTE]
> In Windows Forms applications, Tree List nodes can have associated images. Tree List Editors display these images within the nodes. For more information, refer to the following topic: [](xref:113215).
> In Windows Forms applications, you can also display a collection of items for each category node to the right of the Tree List. For more information, refer to the following topic: [](xref:112838).

If you do not require the hard-coded structure as demonstrated in this example, use the `HCategory` class that implements the `ITreeNode` interface out of the box. For more information, refer to the following topic: [Display a Tree List using the HCategory Class](xref:112839).
