package br.com.ht7.androidmvvm.ui.adapters;

import java.lang.System;

@kotlin.Metadata(mv = {1, 1, 16}, bv = {1, 0, 3}, k = 1, d1 = {"\u0000<\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010 \n\u0002\b\u0002\u0018\u00002\b\u0012\u0004\u0012\u00020\u00020\u0001:\u0001\u0015B\u001d\u0012\u0016\u0010\u0003\u001a\u0012\u0012\u0004\u0012\u00020\u00050\u0004j\b\u0012\u0004\u0012\u00020\u0005`\u0006\u00a2\u0006\u0002\u0010\u0007J\b\u0010\b\u001a\u00020\tH\u0016J\u0018\u0010\n\u001a\u00020\u000b2\u0006\u0010\f\u001a\u00020\u00022\u0006\u0010\r\u001a\u00020\tH\u0016J\u0018\u0010\u000e\u001a\u00020\u00022\u0006\u0010\u000f\u001a\u00020\u00102\u0006\u0010\u0011\u001a\u00020\tH\u0016J\u0014\u0010\u0012\u001a\u00020\u000b2\f\u0010\u0013\u001a\b\u0012\u0004\u0012\u00020\u00050\u0014R\u001e\u0010\u0003\u001a\u0012\u0012\u0004\u0012\u00020\u00050\u0004j\b\u0012\u0004\u0012\u00020\u0005`\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000\u00a8\u0006\u0016"}, d2 = {"Lbr/com/ht7/androidmvvm/ui/adapters/CountryListAdapter;", "Landroidx/recyclerview/widget/RecyclerView$Adapter;", "Lbr/com/ht7/androidmvvm/ui/adapters/CountryListAdapter$CountryListViewHolder;", "countries", "Ljava/util/ArrayList;", "Lbr/com/ht7/androidmvvm/models/Country;", "Lkotlin/collections/ArrayList;", "(Ljava/util/ArrayList;)V", "getItemCount", "", "onBindViewHolder", "", "holder", "position", "onCreateViewHolder", "parent", "Landroid/view/ViewGroup;", "viewType", "update", "newCountries", "", "CountryListViewHolder", "app_debug"})
public final class CountryListAdapter extends androidx.recyclerview.widget.RecyclerView.Adapter<br.com.ht7.androidmvvm.ui.adapters.CountryListAdapter.CountryListViewHolder> {
    private final java.util.ArrayList<br.com.ht7.androidmvvm.models.Country> countries = null;
    
    public final void update(@org.jetbrains.annotations.NotNull()
    java.util.List<br.com.ht7.androidmvvm.models.Country> newCountries) {
    }
    
    @org.jetbrains.annotations.NotNull()
    @java.lang.Override()
    public br.com.ht7.androidmvvm.ui.adapters.CountryListAdapter.CountryListViewHolder onCreateViewHolder(@org.jetbrains.annotations.NotNull()
    android.view.ViewGroup parent, int viewType) {
        return null;
    }
    
    @java.lang.Override()
    public int getItemCount() {
        return 0;
    }
    
    @java.lang.Override()
    public void onBindViewHolder(@org.jetbrains.annotations.NotNull()
    br.com.ht7.androidmvvm.ui.adapters.CountryListAdapter.CountryListViewHolder holder, int position) {
    }
    
    public CountryListAdapter(@org.jetbrains.annotations.NotNull()
    java.util.ArrayList<br.com.ht7.androidmvvm.models.Country> countries) {
        super();
    }
    
    @kotlin.Metadata(mv = {1, 1, 16}, bv = {1, 0, 3}, k = 1, d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u00a2\u0006\u0002\u0010\u0004J\u000e\u0010\r\u001a\u00020\u000e2\u0006\u0010\u000f\u001a\u00020\u0010R\u0016\u0010\u0005\u001a\n \u0007*\u0004\u0018\u00010\u00060\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u0016\u0010\b\u001a\n \u0007*\u0004\u0018\u00010\t0\tX\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u0016\u0010\n\u001a\n \u0007*\u0004\u0018\u00010\u00060\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u000e\u0010\u000b\u001a\u00020\fX\u0082\u0004\u00a2\u0006\u0002\n\u0000\u00a8\u0006\u0011"}, d2 = {"Lbr/com/ht7/androidmvvm/ui/adapters/CountryListAdapter$CountryListViewHolder;", "Landroidx/recyclerview/widget/RecyclerView$ViewHolder;", "view", "Landroid/view/View;", "(Landroid/view/View;)V", "countryCapital", "Landroid/widget/TextView;", "kotlin.jvm.PlatformType", "countryFlag", "Landroid/widget/ImageView;", "countryName", "progressDrawable", "Landroidx/swiperefreshlayout/widget/CircularProgressDrawable;", "bind", "", "country", "Lbr/com/ht7/androidmvvm/models/Country;", "app_debug"})
    public static final class CountryListViewHolder extends androidx.recyclerview.widget.RecyclerView.ViewHolder {
        private final android.widget.TextView countryName = null;
        private final android.widget.ImageView countryFlag = null;
        private final android.widget.TextView countryCapital = null;
        private final androidx.swiperefreshlayout.widget.CircularProgressDrawable progressDrawable = null;
        
        public final void bind(@org.jetbrains.annotations.NotNull()
        br.com.ht7.androidmvvm.models.Country country) {
        }
        
        public CountryListViewHolder(@org.jetbrains.annotations.NotNull()
        android.view.View view) {
            super(null);
        }
    }
}