var infScroll = new InfiniteScroll( '.scroll-container', {
  path: function() {
    pageNumber = this.pageIndex + 1;
    return '/?page=' + pageNumber;
  },
  append: '.grid-item',
  status: '.page-load-status',
  history: false,
  scrollThreshold: 400,
});
