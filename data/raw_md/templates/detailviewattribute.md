```csharp
public class Contact : BaseObject {
    [DetailViewLayoutAttribute(LayoutColumnPosition.Left)]
    public virtual string FirstName { get; set; }
    [DetailViewLayoutAttribute(LayoutColumnPosition.Right)]
    public virtual string LastName { get; set; }
    [DetailViewLayoutAttribute("FullName", 0)]
    public string FullName {
        get { return FirstName + " " + LastName; }
    }
    [DetailViewLayoutAttribute(LayoutColumnPosition.Left)]
    public virtual string Email { get; set; }
    [DetailViewLayoutAttribute(LayoutColumnPosition.Right)]
    public virtual Contact Manager { get; set; }
    [DetailViewLayoutAttribute(LayoutColumnPosition.Left)]
    public virtual DateTime? Birthday { get; set; }
    [FieldSize(FieldSizeAttribute.Unlimited)]
    [DetailViewLayoutAttribute("NotesAndRemarks", LayoutGroupType.TabbedGroup, 100)]
    public virtual string Notes { get; set; }
    [FieldSize(FieldSizeAttribute.Unlimited)]
    [DetailViewLayoutAttribute("NotesAndRemarks", LayoutGroupType.TabbedGroup, 100)]
    public virtual string Remarks { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```