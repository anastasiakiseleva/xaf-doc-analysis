---
uid: DevExpress.ExpressApp.Model.DetailViewLayoutAttribute
name: DetailViewLayoutAttribute
type: Class
summary: Applied to business class properties. Specifies the [Detail View layout](xref:112817) options for a target property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property)]
    public class DetailViewLayoutAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Model.DetailViewLayoutAttribute._members
  altText: DetailViewLayoutAttribute Members
- linkId: "112817"
---
In XAF, you can customize the Detail View layout at design-time or runtime using the [Model Editor](xref:112582). Alternatively, you can modify the layout in code using **DetailViewLayoutAttribute**.

This attribute allows you to set the [DetailViewLayoutAttribute.ColumnPosition](xref:DevExpress.ExpressApp.Model.DetailViewLayoutAttribute.ColumnPosition) of the current editor to specify the [DetailViewLayoutAttribute.GroupId](xref:DevExpress.ExpressApp.Model.DetailViewLayoutAttribute.GroupId), [DetailViewLayoutAttribute.GroupType](xref:DevExpress.ExpressApp.Model.DetailViewLayoutAttribute.GroupType) and [DetailViewLayoutAttribute.GroupIndex](xref:DevExpress.ExpressApp.Model.DetailViewLayoutAttribute.GroupIndex) of the group where this editor will be placed.

Consider the following business class. In this example, we use the Entity Framework Code First class, but a similar approach is applicable to XPO classes as well.



```csharp
public class Contact : BaseObject {
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    public string FullName {
        get { return FirstName + " " + LastName; }
    }
    public virtual string Email { get; set; }
    public virtual Contact Manager { get; set; }
    public virtual DateTime? Birthday { get; set; }
    [FieldSize(FieldSizeAttribute.Unlimited)]
    public virtual string Notes { get; set; }
    [FieldSize(FieldSizeAttribute.Unlimited)]
    public virtual string Remarks { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

The Detail View groups **SimpleEditors** in two columns if there are more than four editors and places **SizeableEditors** one by one. The image below shows this default layout:

![DetailViewLayoutAttributes_Before](~/images/detailviewlayoutattributes_before120490.png)

The code below uses the **DetailViewLayoutAttribute** to customize the layout:

[!include[detailviewattribute](~/templates/detailviewattribute.md)]


> [!NOTE]
> If several properties have the same _groupId_ values, their other parameters should be the same as well.

As a result, the layout is changed in accordance with the specified parameters of **DetailViewLayoutAttribute**.

![DetailViewLayoutAttributes_After](~/images/detailviewlayoutattributes_after120488.png)
