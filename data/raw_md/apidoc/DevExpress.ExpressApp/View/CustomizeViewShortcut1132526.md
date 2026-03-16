---
uid: DevExpress.ExpressApp.View.CustomizeViewShortcut
name: CustomizeViewShortcut
type: Event
summary: Occurs when the [View.CreateShortcut](xref:DevExpress.ExpressApp.View.CreateShortcut) method creates a View Shortcut for the current View.
syntax:
  content: public event EventHandler<CustomizeViewShortcutArgs> CustomizeViewShortcut
seealso: []
---
Handle this event to add custom key/value pairs to View Shortcuts when they are created. Note that you should also add custom keys to the [ViewShortcut.EqualsDefaultIgnoredParameters](xref:DevExpress.ExpressApp.ViewShortcut.EqualsDefaultIgnoredParameters) list, to ensure that they do not break built-in functionalities.

> [!Important]
> Do not modify values corresponding to keys that already exist in newly created View Shortcuts. XAF uses this information internally, and its modification may cause issues with built-in functionalities.

The following example handles the [CustomizeViewShortcut](xref:DevExpress.ExpressApp.View.CustomizeViewShortcut) event to add a filter expression to a List View Shortcut in an XAF application. 

1. Navigate to the _MySolution.Module\Module.cs_ file. In the `Setup` method , subscribe to the `CustomProcessShortcut` event.
2. In this event handler, create a new List View that contains filtered objects and subscribe to the `CustomizeViewShortcut` event.
3. In the event handler, add the List View's filter expression with a custom key to the List View Shortcut.

    **File:** _MySolution.Module\MySolutionModule.cs_

    ```csharp{7,11,14,28,39}
    using DevExpress.Data.Filtering;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    // ...
    namespace MySolution.Module;
    public sealed class MySolutionModule : ModuleBase {
        public const string CustomFilterKey = "CustomFilter";

        public override void Setup(XafApplication application) {
            base.Setup(application);
            application.CustomProcessShortcut += Application_CustomProcessShortcut;
        }
        // ...
        private void Application_CustomProcessShortcut(object sender, CustomProcessShortcutEventArgs e) {
            XafApplication application = (XafApplication)sender;
            if (e.Shortcut.ContainsKey(CustomFilterKey)) {
                IModelListView listViewModel = application.FindModelView(e.Shortcut.ViewId) as IModelListView;
                if (listViewModel != null) {
                    string filterString = Uri.UnescapeDataString(e.Shortcut[CustomFilterKey]);
                    CriteriaOperator filter = CriteriaOperator.Parse(filterString);
                    e.View = CreateFilteredView(application, listViewModel.ModelClass.TypeInfo.Type,
                        listViewModel.Id, filter);
                    e.Handled = true;
                }
            }
        }

        public static ListView CreateFilteredView(XafApplication application, Type objectType,
            string viewId, CriteriaOperator filter) {
            IObjectSpace objectSpace = application.CreateObjectSpace(objectType);
            CollectionSourceBase source = application.CreateCollectionSource(objectSpace, objectType, viewId);

            ListView listView = application.CreateListView(viewId, source, true);
            listView.CollectionSource.Criteria[CustomFilterKey] = filter;
            listView.CustomizeViewShortcut += ListView_CustomizeViewShortcut;
            return listView;
        }

        private static void ListView_CustomizeViewShortcut(object sender, CustomizeViewShortcutArgs e) {
            ListView listView = (ListView)sender;

            if (listView.CollectionSource.Criteria.ContainsKey(CustomFilterKey)) {
                CriteriaOperator criteria = listView.CollectionSource.Criteria[CustomFilterKey];
                if (!ReferenceEquals(criteria, null)) {
                    string filterString = Uri.EscapeDataString(criteria.ToString());
                    e.ViewShortcut[CustomFilterKey] = filterString;
                }
            }
        }
        // ... 
    }
    ```
4. In the _MySolution.Module\Controllers_ folder, create a View Controller that displays the filtered View.

    **File:** _MySolution.Blazor.Server\Controllers\FilteredEmployeesController.cs_

    ```csharp
    using DevExpress.Data.Filtering;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using MySolution.Module;
    using MySolution.Module.BusinessObjects;

    namespace MySolution.Blazor.Server.Controllers;

    public class FilteredEmployeesController : ObjectViewController<ObjectView, Employee> {
        private SimpleAction showMyEmployeesAction;
        
        public FilteredEmployeesController() {
            // Create an action that shows filtered contacts
            showMyEmployeesAction = new SimpleAction(this, "ShowMyEmployees", 
                DevExpress.Persistent.Base.PredefinedCategory.View) {
                Caption = "Show My Managed Employees",
                SelectionDependencyType = SelectionDependencyType.RequireSingleObject
            };
            showMyEmployeesAction.Execute += ShowMyEmployeesAction_Execute;
        }

        private void ShowMyEmployeesAction_Execute  (object sender, SimpleActionExecuteEventArgs e) {
            Employee currentEmployee = (Employee)e.SelectedObjects[0];        
            CriteriaOperator filter = CriteriaOperator.Parse("Manager.ID = ?", currentEmployee.ID);        
            string viewId = Application.GetListViewId(typeof(Employee));        
            ListView filteredView = MainDemoModule.CreateFilteredView(
                Application, 
                typeof(Employee), 
                viewId, 
                filter);        
            e.ShowViewParameters.CreatedView = filteredView;
        }
    }
    ```

> [!NOTE]
> If a filter expression contains special characters (blanks or punctuation marks) it can be misinterpreted in an HTTP stream. To avoid this, use the [HttpUtility.UrlEncode](https://learn.microsoft.com/en-us/dotnet/api/system.web.httputility.urlencode) method to write a criteria string to a `ViewShortcut` and the [HttpUtility.UrlDecode](https://learn.microsoft.com/en-us/dotnet/api/system.web.httputility.urldecode) method to get a `CriteriaOperator` from this ViewShortcut.


