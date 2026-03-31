---
uid: "404700"
title: "How to: Show a Custom Data-Bound Control in an XAF View (Blazor) - Current Object Data"
---
# How to: Show a Custom Data-Bound Control in an XAF View (Blazor) - Current Object Data

This article explains how to create a reusable View Item that uses data from the View's current object. Before starting, review the [!tutorial[ How to: Show a Custom Data-Bound Control in an XAF View (Blazor) - External Data](xref:404698)] tutorial on the basic steps.

![|DevExpress XAF - A Custom Data-Bound Control](~/images/custom-data-bound-control-blazor-advanced-result.png)

## Create a Razor Component

In this example, you create a Razor component based on [DxAccordion](xref:DevExpress.Blazor.DxAccordion). The new component displays employees assigned to a particular department.

To add this component to your project, follow the steps below:

1. In the **Solution Explorer**, right-click your project's name and select **Add** | **New Item…** from the context menu.
2. Specify a component name (`DepartmentViewer.razor`).
3. Add the following code to the created file.

    [!include[<MainDemo.Blazor.Server\\DepartmentViewer.razor>](~/templates/platform_specific_file_path.md)]

    # [Razor](#tab/tabid-razor)

    ```Razor
    @using DevExpress.ExpressApp
    @using DevExpress.ExpressApp.Blazor.Editors
    @using MainDemo.Module.BusinessObjects;
    @using DevExpress.Blazor;

    @implements IDisposable

    @if (ViewItem.CurrentObject is Department department) {
        <p>Department name: <DxTextBox @bind-Text="@department.Title" /></p>
        <p>Department head: @department.DepartmentHead?.FullName</p>
        <p>Department description: @department.Description</p>
        <DxAccordion ExpandMode="AccordionExpandMode.SingleOrNone"
        style="max-width: 600px"
        AnimationType="LayoutAnimationType.Slide">
            <Items>
                @if (department.Employees is not null) {
                    @foreach (var employee in department.Employees) {
                        <DxAccordionItem Text="@employee.FullName" @key="employee">
                            <ContentTemplate>
                                <div style="display: flex;">
                                    <div style="flex: 1 0 0;">
                                        <div><b>Full name:</b> @employee.FullName</div>
                                        <div><b>Email address:</b> @employee.Email</div>
                                        <div><b>Position:</b> @employee.Position</div>
                                        <div><b>Office:</b> @employee.Department.Office</div>
                                        @if (employee.Manager is not null) {
                                            <div><b>Manager:</b> @employee.Manager.FullName</div>
                                        }
                                    </div>
                                    <div style="flex: 1 0 0; display: flex; justify-content: end;">
                                        @if (employee.Photo is not null) {
                                            <div style="flex: 1 0 0; display: flex; justify-content: end;">
                                                <img src="@($"data:image/png;base64,{Convert.ToBase64String(employee.Photo)}")"
                                                style="max-width: 300px; max-height: 300px;">
                                            </div>
                                        }
                                    </div>
                                </div>
                            </ContentTemplate>
                        </DxAccordionItem>
                    }
                }
            </Items>
        </DxAccordion>
    } else {
        <div>No selected department.</div>
    }

    @code {
        [CascadingParameter] public BlazorControlViewItem ViewItem { get; set; }

        protected override void OnInitialized() {
            base.OnInitialized();
            ViewItem.CurrentObjectChanged += View_CurrentObjectChanged;
            ViewItem.ObjectSpace.ObjectChanged += ObjectSpace_ObjectChanged;
        }
        private void ObjectSpace_ObjectChanged(object sender, ObjectChangedEventArgs args) {
            if (args.Object == ViewItem.CurrentObject) {
                InvokeAsync(StateHasChanged);
            }
        }
        private void View_CurrentObjectChanged(object sender, EventArgs args) => InvokeAsync(StateHasChanged);
        void IDisposable.Dispose() {
            ViewItem.CurrentObjectChanged -= View_CurrentObjectChanged;
            ViewItem.ObjectSpace.ObjectChanged -= ObjectSpace_ObjectChanged;
        } 
    }
    ```
    ***

4. In the **Properties** window, set this file's `Build Action` to `Content`.

5. Rebuild your solution.

The component in this example uses the `CascadingParameter` of `DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem` to access an `ObjectSpace` instance. It uses the [Object Space API](xref:113711) to read the required data and then initialize the data source or refresh the data if necessary.

## Change the Default Detail View for the Department List View

1. In the Blazor application project, double-click the _Model.xafml_ file to start the [Model Editor](xref:112582). Right-click the **Views** node and choose **Add… | DetailView**.

    ![|DevExpress XAF - Add a View](~/images/custom-data-bound-control-blazor-advanced-add-view.png)

2. Set the `Id` property to `CustomDepartment_DetailView` and the `ModelClass` property to `MainDemo.Module.BusinessObjects.Department`.

    ![|DevExpress XAF - Specify a View ID](~/images/custom-data-bound-control-blazor-advanced-view-id.png)

3. Right-click the **Views | MainDemo.Module.BusinessObjects | Department | CustomDepartment_DetailView | Items** node and choose **Add… | ControlDetailItem**.

    ![|DevExpress XAF - Add a Detail View Item](~/images/custom-data-bound-control-blazor-advanced-add-detail-view-item.png)

4. Set the `Id` property to `DepartmentViewItem` and the [IModelControlDetailItem.ControlTypeName](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName) property to the type of the Razor Component you created (for example, `MainDemo.Blazor.Server.DepartmentViewer`).

5. Navigate to the **Views | MainDemo.Module.BusinessObjects | Department | Department_ListView** node. In the **DetailView** drop-down list, select **CustomDepartment_DetailView**.

    ![|DevExpress XAF - Change a Default Detail View](~/images/custom-data-bound-control-blazor-advanced-change-default-detail-view.png)    

6. Run your Blazor application, navigate to the **Department** List View, open any Detail View, and see the result.

    ![|DevExpress XAF - A Custom Data-Bound Control](~/images/custom-data-bound-control-blazor-advanced-result.png)
