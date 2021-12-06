import { TestBed } from '@angular/core/testing';

import { ComunicacionbackendService } from './comunicacionbackend.service';

describe('ComunicacionbackendService', () => {
  let service: ComunicacionbackendService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ComunicacionbackendService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
