package br.com.ht7.androidmvvm.di.components;

import java.lang.System;

@kotlin.Metadata(mv = {1, 1, 16}, bv = {1, 0, 3}, k = 1, d1 = {"\u0000\u001c\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\bg\u0018\u00002\u00020\u0001J\u0010\u0010\u0002\u001a\u00020\u00032\u0006\u0010\u0004\u001a\u00020\u0005H&J\u0010\u0010\u0002\u001a\u00020\u00032\u0006\u0010\u0006\u001a\u00020\u0007H&\u00a8\u0006\b"}, d2 = {"Lbr/com/ht7/androidmvvm/di/components/CountryApiComponent;", "", "inject", "", "service", "Lbr/com/ht7/androidmvvm/models/CountryService;", "viewModel", "Lbr/com/ht7/androidmvvm/viewmodels/ListViewModel;", "app_debug"})
@dagger.Component(modules = {br.com.ht7.androidmvvm.di.modules.ApiModule.class})
public abstract interface CountryApiComponent {
    
    public abstract void inject(@org.jetbrains.annotations.NotNull()
    br.com.ht7.androidmvvm.models.CountryService service);
    
    public abstract void inject(@org.jetbrains.annotations.NotNull()
    br.com.ht7.androidmvvm.viewmodels.ListViewModel viewModel);
}