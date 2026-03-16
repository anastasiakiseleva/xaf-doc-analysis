---
uid: "112919"
seealso:
- linkId: "112998"
title: 'How to: Filter Large List Views With Auto Filter Row'
owner: Ekaterina Kiseleva
---
# How to: Filter Large List Views With Auto Filter Row

This topic demonstrates how to use the Auto Filter Row functionality to prevent a grid control from displaying an entire List View collection in ASP.NET Core Blazor and Windows Forms applications.

Imagine a List View bound to a database table with a large amount of data. When a grid control contains millions of records, users often do not need to display this data even if virtual paging is enabled for [better performance](xref:113683) and usability. Instead, they need an application to initially display an empty List View and allow them to filter or search data on demand. All users can benefit from this design, since it reduces the database server and network load because the application does not need to retrieve large amounts of data from the database.

## Step-by-Step Instructions

1. In the **YourSolutionName.Module** project, invoke the [Model Editor](xref:112582) and navigate to the required **Views** | **\<ListView>** node.

2. Set the [IModelListViewShowAutoFilterRow.ShowAutoFilterRow](xref:DevExpress.ExpressApp.SystemModule.IModelListViewShowAutoFilterRow.ShowAutoFilterRow) property to `true` and the [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) property to `Server`.

3. In **Solution Explorer**, navigate to a platform-specific project in Windows Forms or ASP.NET Core Blazor application.

4. Add a [View Controller](xref:112621) to the _Controllers_ folder.

5. Inherit the Controller from the `ObjectViewController<ViewType, ObjectType>` class and override the `OnViewControlsCreated` method as demonstrated in the following code example:

	# [ASP.NET Core Blazor](#tab/tabid-blazor)

	```csharp
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.Blazor.Editors;
	using DevExpress.Data.Filtering;
	using Microsoft.AspNetCore.Components;
	using DevExpress.Blazor;
	using YourApplicationName.Module.BusinessObjects;

	namespace YourApplicationName.Blazor.Server.Controllers;

	public class BlazorAutoFilterRowController : ObjectViewController<ListView, TargetClassName> {
		private const string FalseCriteriaKey = "FalseCriteria";
		private CriteriaOperator FalseCriteria = CriteriaOperator.Parse("1=0");

		protected override void OnViewControlsCreated() {
			base.OnViewControlsCreated();
			if (View.Editor is DxGridListEditor gridListEditor) {
				View.CollectionSource.Criteria[FalseCriteriaKey] = FalseCriteria;
				gridListEditor.GridModel.FilterCriteriaChanged = 
				EventCallback.Factory.Create<GridFilterCriteriaChangedEventArgs>(this, args => {
					if (ReferenceEquals(args.FilterCriteria, null)) {
						View.CollectionSource.Criteria[FalseCriteriaKey] = FalseCriteria;
					}
					else if (View.CollectionSource.Criteria.ContainsKey(FalseCriteriaKey)) {
						View.CollectionSource.Criteria.Remove(FalseCriteriaKey);
					}
				});
			}
		}
	}
	```

	# [Windows Forms](#tab/tabid-winforms)
	```csharp
	using DevExpress.ExpressApp;
	using DevExpress.Data.Filtering;
	using DevExpress.ExpressApp.Win.Editors;
	using DevExpress.XtraGrid.Views.Base;
	using YourApplicationName.Module.BusinessObjects;

	namespace YourApplicationName.Win.Controllers;

	public class WinAutoFilterRowController : ObjectViewController<DevExpress.ExpressApp.ListView, TargetClassName> {
		private const string FalseCriteriaKey = "FalseCriteria";
		private CriteriaOperator FalseCriteria = CriteriaOperator.Parse("1=0");
		protected override void OnViewControlsCreated() {
			base.OnViewControlsCreated();
			if (View.Editor is GridListEditor gridListEditor) {
				View.CollectionSource.Criteria[FalseCriteriaKey] = FalseCriteria;
				gridListEditor.GridView.ActiveFilter.Changed += (s, e) => {
					if (((ViewFilter)s!).IsEmpty) {
						View.CollectionSource.Criteria[FalseCriteriaKey] = FalseCriteria;
					}
					else if (View.CollectionSource.Criteria.ContainsKey(FalseCriteriaKey)) {
						View.CollectionSource.Criteria.Remove(FalseCriteriaKey);
					}
				};
			}
		}
	}
	```
	***

	If you did not specify criteria to filter List View data, the grid control retrieves all existing objects. To prevent this behavior, set a false criterion for the List View's [Collection Source](xref:DevExpress.ExpressApp.CollectionSource).

6. Run the application. The List View with enabled Auto Filter Row should not display any objects.

   ASP.NET Core Blazor
   :   ![|Auto Filter Row with False Criteria in ASP.NET Core Blazor, DevExpress|](~/images/filter-large-listview-collection-blazor-devexpress.png)

   Windows Forms
   :   ![Auto Filter Row with False Criteria in Windows Forms, DevExpress](~/images/filter-large-listview-collection-winforms-devexpress.png)
