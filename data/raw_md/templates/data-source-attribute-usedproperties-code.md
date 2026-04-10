# [C#](#tab/tabid-csharp-efcore)

```csharp{11,18,24}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations.Schema;

public class Order : BaseObject {
    public virtual int OrderId { get; set; }
    public virtual Product Product { get; set; }
    // Specify that AvailableAccessories must be used as a data source property,
    // and the Product and IncludeGlobalAccessories properties are used in calculations.
    [DataSourceProperty(nameof(AvailableAccessories), nameof(Product), nameof(IncludeGlobalAccessories))]
    public virtual Accessory Accessory { get; set; }

    [NotMapped, Browsable(false)] // Prohibits showing the AvailableAccessories collection separately 
    public virtual IList<Accessory> AvailableAccessories {
        get {
            IQueryable<Accessory> available;
            if (Product == null) {
                // Show only Global Accessories when the Product is not specified 
                available = ObjectSpace.GetObjectsQuery<Accessory>().Where(t => t.IsGlobal == true);
            }
            else {
                // Leave only the current Product's Accessories in the availableAccessories collection 
                if (IncludeGlobalAccessories == false) {
                    available = ObjectSpace.GetObjectsQuery<Accessory>().Where(t => t.Product == Product);
                }
                else {
                    available = ObjectSpace.GetObjectsQuery<Accessory>().Where(t => t.Product == Product || t.IsGlobal == true);
                }
            }
            return available.ToList();
        }
    }
    public virtual bool IncludeGlobalAccessories { get; set; }
}
```
***