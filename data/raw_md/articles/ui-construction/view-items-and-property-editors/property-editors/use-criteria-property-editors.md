---
uid: "113143"
seealso:
- linkId: "113564"
- linkId: "112701"
- linkId: "113014"
- linkId: DevExpress.ExpressApp.Editors.EditorAliases
title: 'How to: Enable Database Storage for User-Defined Criteria that Filter a List View'
owner: Anastasiya Kisialeva
---
# How to: Enable Database Storage for User-Defined Criteria that Filter a List View

This topic demonstrates how to design and save filter [criteria](xref:113564) at runtime in an XAF application. The scenario consists of two steps:

1. Define the `FilteringCriterion` business class that implements filter criteria for a List View.
2. Create a custom [View Controller](xref:112621) that contains an [Action](xref:112622) used to filter the List View.

> [!NOTE]
> To follow the instructions in this topic, you can use the **MainDemo.NET** application installed with the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_. You can also download the full implementation from the following GitHub page: [How to use Criteria Property Editors](https://github.com/DevExpress-Examples/xaf-how-to-use-criteria-property-editors).

## Step 1 - Define the FilteringCriterion Business Class

1. Add a class to the _BusinessObjects_ folder of the _MainDemo.Module_ project and name it _FilteringCriterion.cs_. Replace auto-generated code with the following class declaration:

    # [C# (EF Core)](#tab/tabid-csharp-ef)

    ```csharp
    using System.ComponentModel;
    using System.ComponentModel.DataAnnotations.Schema;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.DC;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    
    namespace MainDemo.Module.BusinessObjects {
        [DefaultClassOptions, ImageName("Action_Filter")]
        public class FilteringCriterion : BaseObject {
            private Type objectType;
    
            public virtual string Description { get; set; }
    
            [Browsable(false)]
            public virtual string ObjectTypeName {
                get { return objectType == null ? string.Empty : objectType.FullName; }
                set {
                    ITypeInfo typeInfo = XafTypesInfo.Instance.FindTypeInfo(value);
                    objectType = typeInfo == null ? null : typeInfo.Type;
                }
            }
    
            [NotMapped, ImmediatePostData]
            public Type ObjectType {
                get { return objectType; }
                set {
                    if(objectType == value)
                        return;
                    objectType = value;
                    Criterion = string.Empty;
                }
            }
    
            [CriteriaOptions(nameof(ObjectType))]
            [FieldSize(FieldSizeAttribute.Unlimited)]
            [EditorAlias(EditorAliases.PopupCriteriaPropertyEditor)]
            public virtual string Criterion { get; set; }
        }
    }
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl;
    using DevExpress.Xpo;
    using System.ComponentModel;

    namespace MainDemo.Module.BusinessObjects {
        [DefaultClassOptions, ImageName("Action_Filter")]
        public class FilteringCriterion : BaseObject {
            public FilteringCriterion(Session session) : base(session) { }

            private string description;
            public string Description {
                get { return description; }
                set { SetPropertyValue<string>(nameof(Description), ref description, value); }
            }

            private string objectTypeName;
            [Browsable(false)]
            public string ObjectTypeName {
                get { return objectTypeName; }
                set {
                    Type type = XafTypesInfo.Instance.FindTypeInfo(value) == null ? null :
                        XafTypesInfo.Instance.FindTypeInfo(value).Type;
                    if (objectType != type) {
                        objectType = type;
                    }
                    if (!IsLoading && value != objectTypeName) {
                        Criterion = string.Empty;
                    }
                    SetPropertyValue<string>(nameof(ObjectTypeName), ref objectTypeName, value);
                }
            }

            private Type objectType;
            [TypeConverter(typeof(LocalizedClassInfoTypeConverter))]
            [ImmediatePostData, NonPersistent]
            public Type ObjectType {
                get { return objectType; }
                set {
                    if (objectType != value) {
                        objectType = value;
                        ObjectTypeName = (value == null) ? null : value.FullName;
                    }
                }
            }

            private string criterion;
            [CriteriaOptions(nameof(ObjectType))]
            [Size(SizeAttribute.Unlimited)]
            [EditorAlias(EditorAliases.PopupCriteriaPropertyEditor)]
            public string Criterion {
                get { return criterion; }
                set { SetPropertyValue<string>(nameof(Criterion), ref criterion, value); }
            }
        }
    }
    ```
    ***

    Objects of this class implement filtering criteria.
    
    The `Description` field contains the text that describes a criterion. These descriptions are used to fill a drop-down list of possible filters.
    
    The `Criterion` property contains a criterion. To use the built-in XAF Criteria Property Editors, the property that contains a criterion must have a [](xref:DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute). The attribute's parameter is the name of an additional `Type` property that specifies the target object type. In this sample, it is the `ObjectType` property. Additionally, an @DevExpress.Persistent.Base.EditorAliasAttribute with the `PopupCriteriaPropertyEditor` alias is applied to the `Criterion` property. This attribute changes the default Property Editor for the property:

    * `PopupFilterPropertyEditor` for ASP.NET Core Blazor applications
    * `PopupCriteriaPropertyEditor` for Windows Forms applications

2. _Optional._ If you use Entity Framework Core, register the `FilteringCriterion` type in `DbContext`:

    ```csharp{15}
    using DevExpress.ExpressApp.Design;
    using DevExpress.ExpressApp.EFCore.DesignTime;
    using DevExpress.Persistent.Base;
    using Microsoft.EntityFrameworkCore;
    using Microsoft.EntityFrameworkCore.Design;

    namespace MainDemo.Module.BusinessObjects;

    //..

    [TypesInfoInitializer(typeof(DbContextTypesInfoInitializer<MainDemoDbContext>))]
    public class MainDemoDbContext : DbContext {
        public MainDemoDbContext(DbContextOptions<MainDemoDbContext> options) : base(options) {
        }
        public DbSet<FilteringCriterion> FilteringCriteria { get; set; }

        // ...
    }
    ```

    [!include[](~/templates/update-ef-core.md)]

## Step 2 - Create a Custom List View Controller

1. Add the following `CriteriaController` class to the _Controllers_ folder of the _MainDemo.Module_ project:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using DevExpress.Persistent.Base;
    using MainDemo.Module.BusinessObjects;
    
    namespace MainDemo.Module.Controllers {
        public class CriteriaController : ViewController<ListView> {
            private SingleChoiceAction filteringCriterionAction;
            public CriteriaController() {
                filteringCriterionAction = new SingleChoiceAction(
                    this, "FilteringCriterion", PredefinedCategory.Filters);
                filteringCriterionAction.Execute += FilteringCriterionAction_Execute;
            }
            protected override void OnActivated() {
                filteringCriterionAction.Items.Clear();
                foreach(FilteringCriterion criterion in ObjectSpace.GetObjects<FilteringCriterion>()) {
                    if(criterion.ObjectType.IsAssignableFrom(View.ObjectTypeInfo.Type)) {
                        filteringCriterionAction.Items.Add(new ChoiceActionItem(criterion.Description, criterion.Criterion));
                    }
                }
                if(filteringCriterionAction.Items.Count > 0) {
                    filteringCriterionAction.Items.Add(new ChoiceActionItem("All", null));
                }
            }
            private void FilteringCriterionAction_Execute(object sender, SingleChoiceActionExecuteEventArgs e) {
                var collectionSource = View.CollectionSource;
                collectionSource.BeginUpdateCriteria();
                collectionSource.Criteria.Clear();
                collectionSource.Criteria[e.SelectedChoiceActionItem.Caption] = ObjectSpace.ParseCriteria(e.SelectedChoiceActionItem.Data as string);
                collectionSource.EndUpdateCriteria();
            }
        }
    }
    ```

    This Controller adds the **FilteringCriterion** [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) and populates the Action's drop-down list with all existing `FilterCriterion` objects whose `ObjectType` matches the type of objects displayed in the current List View.

    The **FilteringCriterion** Action applies the criterion selected in the drop-down list to the List View. To convert the `Criterion` property's value of a `FilterCriterion` object to the `DevExpress.Data.Filtering.CriteriaOperator` object, you need to call the static `CriteriaEditorHelper.GetCriteriaOperator` method. This method takes three parameters. The `string` parameter is the criterion to be converted. The `Type` parameter specifies the object type for which the criterion is constructed. The `ObjectSpace` parameter specifies any [](xref:DevExpress.ExpressApp.IObjectSpace) that contains objects of the specified type.

    > [!NOTE]
    > You should not use the [CriteriaOperator.Parse](xref:DevExpress.Data.Filtering.CriteriaOperator.Parse*) method in this scenario. Criteria Property Editors can generate Criteria Strings containing [Object Parameters](xref:113278), which are specific to XAF and cannot be parsed by `CriteriaOperator.Parse`.

2. Run the application, create several business objects, and then try the **FilteringCriterion** action.

   ASP.NET Core Blazor
   :   ![XAF ASP.NET Core Blazor, Criteria Property Editor, DevExpress](~/images/xaf-blazor-how-to-use-criteria-property-editors-devexpress.png)
   Windows Forms
   :   ![XAF Windows Forms, Criteria Property Editor, DevExpress](~/images/howtousecriteriapropertyeditorswin116208.png)
