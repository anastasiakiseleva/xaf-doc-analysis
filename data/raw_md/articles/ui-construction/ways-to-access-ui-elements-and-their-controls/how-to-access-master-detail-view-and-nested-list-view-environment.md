---
uid: "113161"
seealso:
- linkId: "120092"
title: 'How to: Access Nested List View or Master Detail View Environment (ASP.NET Core Blazor and Windows Forms)'
---

# How to: Access Nested List View or Master Detail View Environment (ASP.NET Core Blazor and Windows Forms)

This topic explains how to use [Controllers](xref:112621) to access a nested [List View](xref:112611#list-view)'s or a master [Detail View](xref:112611#detail-view)'s environment ([Frames](xref:112608), Controllers, [Actions](xref:112622), Objects) in XAF ASP.NET Core Blazor and Windows Forms applications.

The topic describes two scenarios:
    * [How to: Access a Master Detail View's Environment from a Nested List View Controller](#how-to-access-a-master-detail-views-environment-from-a-nested-list-view-controller)
    * [How to: Access a Nested List View's Environment from a Master Detail View Controller](#how-to-access-a-nested-list-views-environment-from-a-detail-view-controller)

This topic uses an **Employee** Detail View and **Tasks** nested List View. You can find the corresponding `Employee` and `DemoTask` business classes in the XAF MainDemo application (_[!include[PathTo_MainDemo](~/templates/path-to-main-demo-ef-core.md)]_).

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor Master Detail View with a Nested List View, DevExpress|](~/images/xaf-blazor-master-detail-view-with-nested-list-view-devexpress.png)
Windows Forms
:   ![XAF ASP.NET Core Blazor Master Detail View with a Nested List View, DevExpress](~/images/xaf-winforms-master-detail-view-with-nested-list-view-devexpress.png)

> [!NOTE]
> XAF creates nested List Views for [collection properties](xref:113568). These properties are often used in [relationships between persistent objects](xref:112654).

## How to: Access a Master Detail View's Environment from a Nested List View Controller

Choose the method most suitable for your scenario:
* [Access a Master Detail View's Frame and its Controllers](#access-a-master-detail-views-frame-and-its-controllers)
* [Access a Master Detail View's Current Object (the View Item Approach)](#access-a-master-detail-views-current-object-the-view-item-approach)
* [Access a Master Detail View's Current Object (the Property Collection Source Approach)](#access-a-master-detail-views-current-object-the-property-collection-source-approach)

If you need to access the master [View](xref:112611) from the [DashboardViewItem](xref:DevExpress.ExpressApp.Editors.DashboardViewItem) or the `DetailPropertyEditor`, use the _Access a Master Detail View's Frame and its Controllers_ approach. See the [E4916](https://github.com/DevExpress-Examples/xaf-how-to-implement-dependent-views-in-a-dashboardview-filter-based-on-selection) article for an example. 

### Access a Master Detail View's Frame and its Controllers

1. In the required project of your application, create a nested List View [Controller](xref:112621) that receives the parent [Frame](xref:112608) in the `AssignMasterFrame` method. Use this Frame to customize its Controllers and [Actions](xref:112622). For more information, refer to the following topic: [](xref:112676).

    > [!NOTE]
    > Nested [List View](xref:112611#list-view) Controllers cannot access the parent Detail View Frame, Controllers, and Actions unless the [Detail View](xref:112611#detail-view)'s Controller passes the Detail View Frame to the nested List View Controller. 

    ```csharp
    using DevExpress.ExpressApp;
    
    namespace MainDemo.Module.Controllers;
    
    public class NestedListViewFrameController : ViewController<ListView> {
        private Frame masterFrame;
        public NestedListViewFrameController() {
            TargetViewNesting = Nesting.Nested;
        }
        public void AssignMasterFrame(Frame masterFrame) {
            this.masterFrame = masterFrame;
            // Use this Frame to get Controllers and Actions. 
        }
    }
    ```

2. In the required project of your application, create a master [Detail View](xref:112611#detail-view) Controller that acquires the Detail View [Frame](xref:112608) and passes it to the `NestedListViewFrameController`. Use the `ListPropertyEditor.FrameChanged` event subscription to ensure the nested List View exists.

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Editors;
    
    namespace MainDemo.Module.Controllers;
    
    public class MasterDetailViewController : ViewController<DetailView> {
        private void PushFrameToNestedController(Frame frame) => frame.GetController<NestedListViewFrameController>()?.AssignMasterFrame(this.Frame);
        private void ListPropertyEditor_FrameChanged(object sender, EventArgs e) => PushFrameToNestedController(((ListPropertyEditor)sender).Frame);
        protected override void OnActivated() {
            base.OnActivated();
            foreach(var listPropertyEditor in View.GetItems<ListPropertyEditor>()) {
                if(listPropertyEditor.Frame is not null) {
                    PushFrameToNestedController(listPropertyEditor.Frame);
                }
                else {
                    listPropertyEditor.FrameChanged += ListPropertyEditor_FrameChanged;
                }
            }
        }
        protected override void OnDeactivated() {
            foreach(var listPropertyEditor in View.GetItems<ListPropertyEditor>()) {
                listPropertyEditor.FrameChanged -= ListPropertyEditor_FrameChanged;
            }
            base.OnDeactivated();
        }
        public MasterDetailViewController() {
            TargetViewType = ViewType.DetailView;
        }
    }
    ```

    > [!TIP]
    > For more information about this technique, refer to the following example on GitHub: [XAF - How to access the master Detail View information from a nested List View controller](https://github.com/DevExpress-Examples/xaf-how-to-access-the-master-detailview-information-from-a-nested-listview-controller).

### Access a Master Detail View's Current Object (the View Item Approach)

1. In the required project of your application, create a nested [List View](xref:112611#list-view) Controller. 
Use the [](xref:DevExpress.ExpressApp.View.CurrentObjectChanged) event to update the master Detail View [Caption](xref:DevExpress.ExpressApp.View.Caption) each time the [CurrentObject](xref:DevExpress.ExpressApp.ListView.CurrentObject) changes. 

    ```csharp
    using DevExpress.ExpressApp;
    using MainDemo.Module.BusinessObjects;
    
    namespace MainDemo.Module.Controllers;
    
    public class AccessParentDetailViewController : ObjectViewController<ListView, DemoTask> {
        public AccessParentDetailViewController() {
            TargetViewNesting = Nesting.Nested;
        }
        private void UpdateDetailViewCaption() {
            if(Frame is NestedFrame frame && View.CurrentObject is DemoTask task) {
                frame.ViewItem.View.Caption = task.Subject;
            }
        }
        private void View_CurrentObjectChanged(object sender, EventArgs e) => UpdateDetailViewCaption();
        protected override void OnActivated() {
            base.OnActivated();
            View.CurrentObjectChanged += View_CurrentObjectChanged;
            UpdateDetailViewCaption();
        }
        protected override void OnDeactivated() {
            base.OnDeactivated();
            View.CurrentObjectChanged -= View_CurrentObjectChanged;
        }
    }
    ```

### Access a Master Detail View's Current Object (the Property Collection Source Approach)

1. In the required project of your application, create a nested [List View](xref:112611#list-view) Controller. The nested List View's [](xref:DevExpress.ExpressApp.ListView.CollectionSource) type is [](xref:DevExpress.ExpressApp.PropertyCollectionSource) because the List View is a [collection property](xref:113568).

2. Handle the [](xref:DevExpress.ExpressApp.PropertyCollectionSource.MasterObjectChanged) event and process the current [](xref:DevExpress.ExpressApp.PropertyCollectionSource.MasterObject) when the master object changes.

    ```csharp
    using DevExpress.ExpressApp;
    using MainDemo.Module.BusinessObjects;
    
    namespace MainDemo.Module.Controllers;
    
    public class AccessMasterObjectController : ObjectViewController<ListView, DemoTask> {
        private void UpdateMasterObject(object masterObject) {
            Employee employee = (Employee)masterObject;
            // Use the master object as required.            
        }
        private void OnMasterObjectChanged(object sender, EventArgs e) => UpdateMasterObject(((PropertyCollectionSource)sender).MasterObject);
        protected override void OnActivated() {
            base.OnActivated();
            if(View.CollectionSource is PropertyCollectionSource collectionSource) {
                collectionSource.MasterObjectChanged += OnMasterObjectChanged;
                if(collectionSource.MasterObject is not null) {
                    UpdateMasterObject(collectionSource.MasterObject);
                }
            }
        }
        protected override void OnDeactivated() {
            if(View.CollectionSource is PropertyCollectionSource collectionSource) {
                collectionSource.MasterObjectChanged -= OnMasterObjectChanged;
            }
            base.OnDeactivated();
        }
        public AccessMasterObjectController() {
            TargetViewNesting = Nesting.Nested;
        }
    }
    ```

## How to: Access a Nested List View's Environment from a Detail View Controller

1. In the required project of your application, create a [Detail View](xref:112611#detail-view) Controller.

2. Handle the [](xref:DevExpress.ExpressApp.View.CurrentObjectChanged) event and use the @DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[]) method to obtain the current nested [List View](xref:112611#list-view)'s [Frame](xref:112608) and object. For more information about the use of `PerformLogicWithCurrentListViewObject` and `PerformLogicInNestedListViewController` methods, refer to the following topic: [Customize Controllers and Actions](xref:112676).

    > [!NOTE]
    > You can also use this technique to customize a [DashboardViewItem](xref:DevExpress.ExpressApp.Editors.DashboardViewItem) and `DetailPropertyEditor` because these View Items contain a Frame with an inner View. For more information, refer to the following example: [XAF - How to implement dependent views in a DashboardView (filter based on selection)](https://github.com/DevExpress-Examples/xaf-how-to-implement-dependent-views-in-a-dashboardview-filter-based-on-selection). 

    ```csharp
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp;
    using MainDemo.Module.BusinessObjects;

    namespace MainDemo.Module.Controllers;

    public class AccessNestedListViewController : ObjectViewController<DetailView, Employee> {
        private void PerformLogicWithCurrentListViewObject(object currentListViewObject) {
            DemoTask task = (DemoTask)currentListViewObject;
            // Use the object in the nested List View as required.
        }
        private void PerformLogicInNestedListViewController(Frame nestedFrame) {
            // Use the nested Frame as required.
        }
        private void NestedListView_SelectionChanged(object sender, EventArgs e) {
            var listView = (ListView)sender;
            PerformLogicWithCurrentListViewObject(listView.CurrentObject);
        }
        private void ProcessListPropertyEditor(ListPropertyEditor listPropertyEditor) {
            var nestedListView = listPropertyEditor.ListView;
            PerformLogicWithCurrentListViewObject(nestedListView.CurrentObject);
            PerformLogicInNestedListViewController(listPropertyEditor.Frame);
            nestedListView.SelectionChanged += NestedListView_SelectionChanged;
        }
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<ListPropertyEditor>(this, ProcessListPropertyEditor, nameof(Employee.Tasks));
        }
    }
    ```
