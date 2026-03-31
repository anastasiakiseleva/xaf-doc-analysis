---
uid: "403258"
title: 'How to: Use a Custom Component to Implement List Editor (Blazor)'
seealso:
- linkId: "113653"
- linkId: "112659"
- linkId: "402189"
---
# How to: Use a Custom Component to Implement List Editor (Blazor)

This scenario implements a custom List Editor that shows images in an ASP.NET Core Blazor application. The List Editor displays a Razor component with custom objects. These objects implement a custom `IPictureItem` interface to store images with captions. 

[!example[How to: Use a Custom Component to Implement List Editor (Blazor)](https://github.com/DevExpress-Examples/xaf-custom-list-editor-blazor)]

![Blazor Custom List Editor](~/images/blazor-custom-list-editor.png)

To add a custom List Editor to your ASP.NET Core Blazor application, [define the required data model](#define-the-data-model) and implement the following components in the ASP.NET Core Blazor [application project](xref:118045) (**YourSolutionName.Blazor.Server**).

* [Razor Component](#razor-component) - to define the required markup.
* [Component Model](#component-model) - to change the state of the component.
* [List Editor](#list-editor) - to integrate the component into your XAF application.

## Define the Data Model

1. In the _CustomEditorEF.Module_ project, create a new interface and name it `IPictureItem`. In this interface, declare the `Image` and `Text` properties. This allows the List Editor to work with different types of objects that implement this interface.

   **File:** _CustomEditorEF.Module\BusinessObjects\IPictureItem.cs_
   # [C#](#tab/tabid-csharp)
   [!codesnippet-cs[dx-examples](xaf-custom-list-editor-blazor/CS/EF/CustomEditorEF/CustomEditorEF.Module/BusinessObjects/IPictureItem.cs)]
   ```cs
   namespace CustomEditorEF.Module.BusinessObjects;
   public interface IPictureItem {
       byte[] Image { get; }
       string Text { get; }
   }

   ```
   ***

2. In the _CustomEditorEF.Module_ project, create a business class that implements the `IPictureItem` interface. Name this class `PictureItem`.

   **File:** _CustomEditorEF.Module\BusinessObjects\PictureItem.cs_
   # [C#](#tab/tabid-csharp-xpo)
   [!codesnippet-cs[dx-examples](xaf-custom-list-editor-blazor/CS/EF/CustomEditorEF/CustomEditorEF.Module/BusinessObjects/PictureItem.cs)]
   ```cs
   using DevExpress.Persistent.Base;
   using DevExpress.Persistent.BaseImpl;
   using DevExpress.Persistent.BaseImpl.EF;

   namespace CustomEditorEF.Module.BusinessObjects;
   [DefaultClassOptions]
   public class PictureItem : BaseObject, IPictureItem {
       [ImageEditor]
       public virtual byte[] Image { get; set; }
       public virtual string Text { get; set; }
   }

   ```
   ***

3. Register the `PictureItems` entity in the `DbContext`:
   
    **File:** _CustomEditorEF.Module\BusinessObjects\CustomEditorEFDbContext.cs_
   
    # [C#](#tab/tabid-csharp-efcore1)
    [!codesnippet-cs[dx-examples](xaf-custom-list-editor-blazor/CS/EF/CustomEditorEF/CustomEditorEF.Module/BusinessObjects/CustomEditorEFDbContext.cs?line=10-11,35,38,44)]
    ```cs
    namespace CustomEditorEF.Module.BusinessObjects;
    
    // ...
    public class CustomEditorEFEFCoreDbContext : DbContext {
    // ...
        public DbSet<PictureItem> PictureItems { get; set; }
        // ...
    }
    ```
    ***

## Razor Component

1. In the _CustomEditorEF.Blazor.Server_ project, create a new [Razor component](https://learn.microsoft.com/en-us/aspnet/core/blazor/components) and name it `PictureItemListView`.

2. Ensure that the component's [`Build Action`](https://learn.microsoft.com/en-us/visualstudio/ide/build-actions) property is set to `Content`.

3. Declare the `Data` component parameter. 

4. Iterate through the `Data` collection and define the markup for each data object. 

    > [!NOTE]
    > The `PictureItemListView` component supports only PNG images.

    **File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\PictureItemListView.razor_

    # [RAZOR](#tab/tabid-razor)
    ```razor
    @using CustomEditorEF.Module.BusinessObjects;
    @using Microsoft.AspNetCore.Components.Web

    @if (Data is not null) {
        <div class="row">
            @foreach (var item in Data) {
                <div class="col-auto">
                    @if (item.Image is null) {
                        <div class="border d-flex justify-content-center align-items-center"
                            style="height:150px; width: 104px;">
                            No image
                        </div>
                    }
                    else {
                        <img src="data:image/png;base64,@Convert.ToBase64String(item.Image)" alt=@item.Text
                            style="height:150px; width: 104px;">
                    }
                    <div class="text-center" style="width: 104px;">
                        @item.Text
                    </div>
                </div>
            }
        </div>
    }

    @code {
        [Parameter]
        public IEnumerable<IPictureItem> Data { get; set; }
    }
    ```
    ***

## Component Model

In the _CustomEditorEF.Blazor.Server_ project, create a `ComponentModelBase` descendant and name it `PictureItemListViewModel`. In this class, declare properties that describe the component.

**File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\PictureItemListViewModel.cs_

# [C#](#tab/tabid-csharp)
```cs
using CustomEditorEF.Module.BusinessObjects;
using DevExpress.ExpressApp.Blazor.Components.Models;
using Microsoft.AspNetCore.Components;

namespace CustomEditorEF.Blazor.Server.Editors.CustomList {
    public class PictureItemListViewModel : ComponentModelBase {
        public IEnumerable<IPictureItem> Data {
            get => GetPropertyValue<IEnumerable<IPictureItem>>();
            set => SetPropertyValue(value);
        }
        public override Type ComponentType => typeof(PictureItemListView);
    }
}
```
***

## List Editor

> [!TIP]
> You can find the full List Editor file code at the end of this topic:  [BlazorCustomListEditor.cs](#full-list-editor-code). 

1. Create a @DevExpress.ExpressApp.Editors.ListEditor descendant and name it `BlazorCustomListEditor`.

2. Apply the following @DevExpress.ExpressApp.Editors.ListEditorAttribute to the `BlazorCustomListEditor` class: `[ListEditor(typeof(IPictureItem))]`. This attribute value makes `BlazorCustomListEditor` the default editor for any `IPictureItem` List View.

3. Add the `ComponentContent` property to create and cache the UI content of the List Editor based on the current View model. For more information, refer to the following topic: [](xref:404767).

    **File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\BlazorCustomListEditor.cs_

    # [C#](#tab/tabid-csharp)
    ```cs
    using System;
    using System.Collections;
    using System.ComponentModel;
    using System.Linq;
    using CustomEditorEF.Module.BusinessObjects;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor;
    using DevExpress.ExpressApp.Blazor.Components;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp.Model;
    using Microsoft.AspNetCore.Components;

    namespace CustomEditorEF.Blazor.Server.Editors.CustomList {
        [ListEditor(typeof(IPictureItem))]
        public class BlazorCustomListEditor : ListEditor, IComponentContentHolder {
        private RenderFragment _componentContent;

        public PictureItemListViewModel ComponentModel { get; private set; }

            public RenderFragment ComponentContent {
                get {
                    _componentContent ??= ComponentModelObserver.Create(ComponentModel, ComponentModel.GetComponentContent());
                    return _componentContent;
                }
            }
        }
    }
    ```
    ***

4. Override the `CreateControlsCore` method to return a `PictureItemListViewModel` instance.
    # [C#](#tab/tabid-csharp)
    ```cs
    [ListEditor(typeof(IPictureItem))]
    public class BlazorCustomListEditor : ListEditor, IComponentContentHolder {
        // ...
        protected override object CreateControlsCore() =>
            ComponentModel = new PictureItemListViewModel();
    }
    ```
    ***

5. Override the `AssignDataSourceToControl` method. In this method, assign the List Editor's data source to the component model. If the data source implements the [`IBindingList`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.ibindinglist) interface, handle data change notifications.

    # [C#](#tab/tabid-csharp)
    ```cs
    [ListEditor(typeof(IPictureItem))]
    public class BlazorCustomListEditor : ListEditor, IComponentContentHolder {
        // ...
        protected override void AssignDataSourceToControl(object dataSource) {
            if(ComponentModel is not null) {
                if(ComponentModel.Data is IBindingList bindingList) {
                    bindingList.ListChanged -= BindingList_ListChanged;
                }
                UpdateDataSource(dataSource);
                if(dataSource is IBindingList newBindingList) {
                    newBindingList.ListChanged += BindingList_ListChanged;
                }
            }
        }

        private void BindingList_ListChanged(object sender, ListChangedEventArgs e) {
            UpdateDataSource(DataSource);
        }
        private void UpdateDataSource(object dataSource) {
            if (ComponentModel is not null) {
                ComponentModel.Data = (dataSource as IEnumerable)?.OfType<IPictureItem>().OrderBy(i => i.Text).ToList<IPictureItem>();
            }
        }
    }
    ```
    ***

    [!NOTE]
    > The editor has a basic data source and UI implementation for demo purposes only and not for large data records (for example, no pagination/virtualization or no support for [DataAccessMode](xref:113683) other than Client). To support large data records or data record projections, you may need to re-implement the `UpdateDataSource`, `GetOrderedObjects`, and related methods using `IQueryable` or other means (not mentioned in this article).

6. Override the @DevExpress.ExpressApp.Editors.ListEditor.BreakLinksToControls method. In this method, reset the component model's data to release resources. Override the @DevExpress.ExpressApp.Editors.ListEditor.Refresh method. In this method, call the `UpdateDataSource` method to update the List Editor when its data is changed.

    # [C#](#tab/tabid-csharp)
    ```cs
    [ListEditor(typeof(IPictureItem))]
    public class BlazorCustomListEditor : ListEditor, IComponentContentHolder {
        public override void BreakLinksToControls() {
            AssignDataSourceToControl(null);
            base.BreakLinksToControls();
        }
        public override void Refresh() => UpdateDataSource(DataSource);
    }
    ```
    ***

7. Override the remaining required members so that the code can compile.

    # [C#](#tab/tabid-csharp)
   ```cs
   [ListEditor(typeof(IPictureItem))]
   public class BlazorCustomListEditor : ListEditor, IComponentContentHolder {
       // ...
       public override SelectionType SelectionType => SelectionType.None;
       public override IList GetSelectedObjects() => Array.Empty<object>();
   }
   ```
    ***

8. Implement utility methods to work with items in a custom List Editor (for example, map between objects and their positions in the list and retrieve the current ordered set of items). Make sure that you implement the `IControlOrderProvider` interface to support the @DevExpress.ExpressApp.SystemModule.RecordsNavigationController that contains the **Previous** and **Next** Actions:

    # [C#](#tab/tabid-csharp)
    ```cs{3}
    //..
    [ListEditor(typeof(IPictureItem))]
    public class BlazorCustomListEditor : ListEditor, IComponentContentHolder, IControlOrderProvider {

        public int GetIndexByObject(object obj) {
            var items = ListHelper.GetList(ComponentModel.Data);
            var index = items.IndexOf(obj);
            if (index == int.MinValue) {
                index = -1;
            }
            return index;
        }
        public object GetObjectByIndex(int index) {
            var items = ListHelper.GetList(ComponentModel.Data);
            return items[index];
        }
        public IList GetOrderedObjects() {
            var orderedObjects = new List<object>();
            var items = ListHelper.GetList(ComponentModel.Data);
            for (var rowVisibleIndex = 0; rowVisibleIndex < items.Count; ++rowVisibleIndex) {
                var record = items[rowVisibleIndex];
                if (record != null) {
                    orderedObjects.Add(record);
                }
            }
            return orderedObjects;
        }
    }
    ```
    ***

## Open a Detail View on Item Click

In its current state, the `BlazorCustomListEditor` can only display `PictureItem` records. To enable record editing in a Detail View, the `PictureItemListView` component needs to notify `BlazorCustomListEditor` that a user clicked on a particular item. The following scenario enables the component model to pass messages between these two entities.


1. Declare an `ItemClick` component parameter for the `PictureItemListView` Razor component. Invoke this callback whenever a user clicks an item.

    **File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\PictureItemListView.razor_

    # [RAZOR](#tab/tabid-razor)
    ```razor{7-8,17-18}
    @using CustomEditorEF.Module.BusinessObjects;
    @using Microsoft.AspNetCore.Components.Web

    @if (Data is not null) {
        <div class="row">
            @foreach (var item in Data) {
                <div class="col-auto" style="cursor: pointer;"
                    @onclick=@(async () => await ItemClick.InvokeAsync(item))>
                    @* unchanged *@
                </div>
            }
        </div>
    }

    @code {
        @*...*@
        [Parameter]
        public EventCallback<IPictureItem> ItemClick { get; set; }
    }
    ```
    ***

2. In _PictureItemListViewModel.cs_, declare the `ItemClick` property. It enables the ASP.NET Core Blazor UI to react to item click events

    **File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\PictureItemListViewModel.cs_

    # [C#](#tab/tabid-csharp)
    ```cs
    // ...
    namespace CustomEditorEF.Blazor.Server.Editors.CustomList {
        public class PictureItemListViewModel : ComponentModelBase {
            // ...
            public EventCallback<IPictureItem> ItemClick {
                get => GetPropertyValue<EventCallback<IPictureItem>>();
                set => SetPropertyValue(value);
            }
        }
    }

    ```
    ***

3. Modify `BlazorCustomListEditor` to react to clicks:
   - Set `SelectionType` to `SelectionType.Full` - this setting allows a user to open the Detail View by click.
   - Modify `GetSelectedObjects()` to return a collection of `IPictureItem`s.
   - Access the Component Model's `ItemClick` property in the newly overridden `OnControlsCreated()` method.
   - Replace previously selected objects with the clicked item and call `OnProcessSelectedItem` to open a Detail View for it.

    **File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\BlazorCustomListEditor.cs_
    # [C#](#tab/tabid-csharp)
    ```cs{5,8-14,16-17}
    //...
    [ListEditor(typeof(IPictureItem))]
    public class BlazorCustomListEditor : ListEditor, IComponentContentHolder, IControlOrderProvider {
        private RenderFragment _componentContent;
        private IPictureItem[] selectedObjects = Array.Empty<IPictureItem>();
        //...

        protected override object CreateControlsCore() {
            ComponentModel = new PictureItemListViewModel();
            ComponentModel.ItemClick = EventCallback.Factory.Create<IPictureItem>(this, (item) => {
                selectedObjects = new IPictureItem[] { item };
                OnProcessSelectedItem();
            });
            return ComponentModel;
        }
        //...
        public override SelectionType SelectionType => SelectionType.Full;
        public override IList GetSelectedObjects() => selectedObjects;
    }
    ```
    ***

> [!NOTE]
> If your editor requires access to Dependency Injection and application services, or you need to access an instance of `XafApplication` and `ObjectSpace`, refer to the following section: [Access ServiceProvider, XafApplication and ObjectSpace to Query and Manipulate Data (Perform CRUD Operations)](#access-serviceprovider-xafapplication-and-objectspace-to-query-and-manipulate-data-perform-crud-operations).

## Implement Multiple Selection

This scenario enables the selection of multiple records in a List View. This is useful when a user needs to bulk-delete items or simultaneously execute other actions for several records.

1. Implement multiple selection in the `PictureItemListView` Razor component:
   - Add a list of items that comprise the selection.
   - Wrap the markup for `IPictureItem` records in [DxCheckBox](xref:DevExpress.Blazor.DxCheckBox`1) components. When the checkbox is ticked or unticked, the selection changes accordingly via the `SelectItem` method, and `BlazorCustomListEditor` is notified of these changes when the `SelectionChanged` event callback is invoked.
   - Ensure that the selection stays up-to-date. When the `PictureItemListView` component is [re-rendered](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle), it builds up a new list of selected items, discarding objects that are no longer present in the new/modified `Data` source. If any changes are found, the List Editor is notified.

    **File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\PictureItemListView.razor_

    # [RAZOR](#tab/tabid-razor)
    ```razor{7-9,14}
    @using CustomEditorEF.Module.BusinessObjects;
    @using Microsoft.AspNetCore.Components.Web

    @if (Data is not null) {
        <div class="row">
            @foreach (var item in Data) {
                <DxCheckBox Checked="@selectedItems.Contains(item)"
                            CssClass="col-auto"
                            CheckedChanged="@(async (bool isSelected) => await SelectItem(item, isSelected))">
                    <div style="cursor: pointer;" @onclick=@(async () => await ItemClick.InvokeAsync(item))>
                        @if (item.Image is null) {
                            <div class="border d-flex justify-content-center align-items-center"
                                style="height:150px; width: 104px;">
                                No image
                            </div>
                        }
                        else {
                            <img src="data:image/png;base64,@Convert.ToBase64String(item.Image)" alt=@item.Text
                                style="height:150px; width: 104px;">
                        }
                        <div class="text-center" style="width: 104px;">
                            @item.Text
                        </div>
                    </div>
                </DxCheckBox>
            }
        </div>
    }

    @code {
        [Parameter] public IEnumerable<IPictureItem> Data { get; set; }
        [Parameter] public EventCallback<IPictureItem> ItemClick { get; set; }
        [Parameter] public EventCallback<IEnumerable<IPictureItem>> SelectionChanged { get; set; }

        private List<IPictureItem> selectedItems = new();

        protected override async Task OnParametersSetAsync() {
            await base.OnParametersSetAsync();
            var newSelectedItems = new List<IPictureItem>();
            if (Data is not null) {
                foreach (var item in Data) {
                    if (selectedItems.Contains(item)) {
                        newSelectedItems.Add(item);
                    }
                }
            }
            if (!newSelectedItems.SequenceEqual(selectedItems)) {
                await SelectionChanged.InvokeAsync(newSelectedItems);
            }
            selectedItems = newSelectedItems;
        }
        private async Task SelectItem(IPictureItem item, bool isSelected) {
            if (isSelected) {
                selectedItems.Add(item);
            }
            else {
                selectedItems.Remove(item);
            }
            await SelectionChanged.InvokeAsync(selectedItems);
        }
    }
    ```
    ***

2. Similar to adding support for item click events, add the selection-related property to the Component Model class:

    **File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\PictureItemListViewModel.cs_

    # [C#](#tab/tabid-csharp)
    ```cs
    // ...
    namespace CustomEditorEF.Blazor.Server.Editors.CustomList {
        public class PictureItemListViewModel : ComponentModelBase {
            // ...
            public EventCallback<IEnumerable<IPictureItem>> SelectionChanged {
                get => GetPropertyValue<EventCallback<IEnumerable<IPictureItem>>>();
                set => SetPropertyValue(value);
            }
        }
    }
    ```
    ***

3. Modify `BlazorCustomListEditor` to process the new event:

    **File:** _CustomEditorEF.Blazor.Server\Editors\CustomList\BlazorCustomListEditor.cs_

    # [C#](#tab/tabid-csharp)
    ```cs{9,12-15}
    //...
    [ListEditor(typeof(IPictureItem))]
    public class BlazorCustomListEditor : ListEditor, IComponentContentHolder, IControlOrderProvider {
        //...
        protected override object CreateControlsCore() {
            ComponentModel = new PictureItemListViewModel();
            ComponentModel.ItemClick = EventCallback.Factory.Create<IPictureItem>(this, (item) => {
                selectedObjects = new IPictureItem[] { item };
                OnSelectionChanged();
                OnProcessSelectedItem();
            });
            ComponentModel.SelectionChanged = EventCallback.Factory.Create<IEnumerable<IPictureItem>>(this, (items) => {
                selectedObjects = items.ToArray();
                OnSelectionChanged();
            });
            return ComponentModel;
        }
    }
    ```
    ***

### Full List Editor Code

The full _BlazorCustomListEditor.cs_ file code:

# [C#](#tab/tabid-csharp)
[!codesnippet-cs[dx-examples](xaf-custom-list-editor-blazor/CS/EF/CustomEditorEF/CustomEditorEF.Blazor.Server/Editors/CustomList/BlazorCustomListEditor.cs)]
```cs
using CustomEditorEF.Module.BusinessObjects;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor;
using DevExpress.ExpressApp.Blazor.Components;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Utils;
using Microsoft.AspNetCore.Components;
using System.Collections;
using System.ComponentModel;

namespace CustomEditorEF.Blazor.Server.Editors.CustomList {
    [ListEditor(typeof(IPictureItem))]
    public class BlazorCustomListEditor : ListEditor, IComponentContentHolder, IControlOrderProvider {
        private RenderFragment _componentContent;
        private IPictureItem[] selectedObjects = Array.Empty<IPictureItem>();

        public PictureItemListViewModel ComponentModel { get; private set; }

        public RenderFragment ComponentContent {
            get {
                _componentContent ??= ComponentModelObserver.Create(ComponentModel, ComponentModel.GetComponentContent());
                return _componentContent;
            }
        }

        public BlazorCustomListEditor(IModelListView model) : base(model) { }

        private void BindingList_ListChanged(object sender, ListChangedEventArgs e) {
            UpdateDataSource(DataSource);
        }

        private void UpdateDataSource(object dataSource) {
            if(ComponentModel is not null) {
                ComponentModel.Data = (dataSource as IEnumerable)?.OfType<IPictureItem>().OrderBy(i => i.Text).ToList<IPictureItem>();
            }
        }

        protected override object CreateControlsCore() {
            ComponentModel = new PictureItemListViewModel();
            ComponentModel.ItemClick = EventCallback.Factory.Create<IPictureItem>(this, (item) => {
                selectedObjects = new IPictureItem[] { item };
                OnSelectionChanged();
                OnProcessSelectedItem();
            });
            ComponentModel.SelectionChanged = EventCallback.Factory.Create<IEnumerable<IPictureItem>>(this, (items) => {
                selectedObjects = items.ToArray();
                OnSelectionChanged();
            });
            return ComponentModel;
        }

        protected override void AssignDataSourceToControl(object dataSource) {
            if(ComponentModel is not null) {
                if(ComponentModel.Data is IBindingList bindingList) {
                    bindingList.ListChanged -= BindingList_ListChanged;
                }
                UpdateDataSource(dataSource);
                if(dataSource is IBindingList newBindingList) {
                    newBindingList.ListChanged += BindingList_ListChanged;
                }
            }
        }

        public override void BreakLinksToControls() {
            AssignDataSourceToControl(null);
            base.BreakLinksToControls();
        }

        public override void Refresh() => UpdateDataSource(DataSource);

        public override SelectionType SelectionType => SelectionType.Full;

        public override IList GetSelectedObjects() => selectedObjects;

        public int GetIndexByObject(object obj) {
            var items = ListHelper.GetList(ComponentModel.Data);
            var index = items.IndexOf(obj);
            if (index == int.MinValue) {
                index = -1;
            }
            return index;
        }
        public object GetObjectByIndex(int index) {
            var items = ListHelper.GetList(ComponentModel.Data);
            return items[index];
        }
        public IList GetOrderedObjects() {
            var orderedObjects = new List<object>();
            var items = ListHelper.GetList(ComponentModel.Data);
            for (var rowVisibleIndex = 0; rowVisibleIndex < items.Count; ++rowVisibleIndex) {
                var record = items[rowVisibleIndex];
                if (record != null) {
                    orderedObjects.Add(record);
                }
            }
            return orderedObjects;
        }
    }
}

```

***
[`ListEditor`]: xref:DevExpress.ExpressApp.Editors.ListEditor 
[`RenderFragment`]: https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.renderfragment
[`BreakLinksToControls`]: xref:DevExpress.ExpressApp.Editors.ListEditor.BreakLinksToControls
[`SelectionType`]: xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionType
[`GetSelectedObjects`]: xref:DevExpress.ExpressApp.Editors.ListEditor.GetSelectedObjects
[`IBindingList`]: https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.ibindinglist

The custom List Editor supports only the [Client](xref:118449) data access mode. Set the Client data access mode in the static `DataAccessModeHelper.RegisterEditorSupportedModes` method as described in the [Specify Data Access Mode](xref:113683#specify-data-access-mode) section of the following topic: [List View Data Access Modes](xref:113683).
**File**: _CustomEditorEF.Blazor.Server\BlazorModule.cs_

# [C#](#tab/tabid-csharp)

```cs{1,5-6}
using DevExpress.ExpressApp.Utils;
// ...
public sealed class CustomEditorEFBlazorModule : ModuleBase {
    public CustomEditorEFBlazorModule() {
        DataAccessModeHelper.RegisterEditorSupportedModes(typeof(BlazorCustomListEditor),
                                 new[] { CollectionSourceDataAccessMode.Client });
    }
    // ...
}
```

***

## Access ServiceProvider, XafApplication and ObjectSpace to Query and Manipulate Data (Perform CRUD Operations)

A custom List Editor may require access to the application object or the List View Collection Source (the List View data source). If so, implement the `IComplexListEditor` interface as shown in the following topic: @DevExpress.ExpressApp.Editors.IComplexListEditor. 

Use the [IComplexListEditor.Setup](xref:DevExpress.ExpressApp.Editors.IComplexListEditor.Setup(DevExpress.ExpressApp.CollectionSourceBase,DevExpress.ExpressApp.XafApplication)) method to get the @DevExpress.ExpressApp.XafApplication and @DevExpress.ExpressApp.CollectionSourceBase objects. The @DevExpress.ExpressApp.CollectionSourceBase class is the base class for Collection Source classes that allow you to manipulate ObjectSpace data.

You can also obtain an `IServiceProvider` instance for Dependency Injection needs by accessing the [XafApplication.ServiceProvider](xref:DevExpress.ExpressApp.XafApplication.ServiceProvider) property.